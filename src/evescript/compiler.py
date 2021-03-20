from antlr4 import CommonTokenStream, ParseTreeVisitor
from antlr4.error.ErrorListener import ErrorListener
from antlr4.error.Errors import ParseCancellationException
from antlr4.InputStream import InputStream

from .eveparser.parser_output.EveScriptLexer import EveScriptLexer
from .eveparser.parser_output.EveScriptParser import EveScriptParser


class ThrowingErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        ex = ParseCancellationException(f'line {line}: {column} {msg}')
        ex.line = line
        ex.column = column
        raise ex


class EveScriptCompiler(ParseTreeVisitor):

    def compile(self, script, raise_exceptions=False):

        input_stream = InputStream(script)

        lexer = EveScriptLexer(input_stream)

        if raise_exceptions:
            lexer.removeErrorListeners()
            lexer.addErrorListener(ThrowingErrorListener())

        token_stream = CommonTokenStream(lexer)

        parser = EveScriptParser(token_stream)

        if raise_exceptions:
            parser.removeErrorListeners()
            parser.addErrorListener(ThrowingErrorListener())

        tree = parser.script()

        return self.visitScript(tree)

    # Visit a parse tree produced by EveScriptParser#script.
    def visitScript(self, ctx: EveScriptParser.ScriptContext):
        return {
            'statements': [self.visitStatement(statement) for statement in ctx.statement()],
        }

    # Visit a parse tree produced by EveScriptParser#condition.
    def visitStatement(self, ctx: EveScriptParser.StatementContext):
        return {
            'if': self.visitExpr(ctx.expr()),
            'then': [self.visitAction(action) for action in ctx.action()],
        }

    # Visit a parse tree produced by EveScriptParser#expr.
    def visitExpr(self, ctx: EveScriptParser.ExprContext):

        if ctx.getChildCount() == 3 and ctx.getChild(1).getText() == '||':
            # expr: term '||' expr
            return {
                'operator': '||',
                'operands': [
                    self.visitTerm(ctx.term()),
                    self.visitExpr(ctx.expr()),
                ],
            }
        else:
            # expr: term
            return self.visitTerm(ctx.term())

    # Visit a parse tree produced by EveScriptParser#term.
    def visitTerm(self, ctx: EveScriptParser.TermContext):
        if ctx.getChildCount() == 3 and ctx.getChild(1).getText() == '&&':
            # term: factor '||' term
            return {
                'operator': '&&',
                'operands': [
                    self.visitFactor(ctx.factor()),
                    self.visitTerm(ctx.term()),
                ],
            }
        else:
            # term: factor
            return self.visitFactor(ctx.factor())

    # Visit a parse tree produced by EveScriptParser#factor.
    def visitFactor(self, ctx: EveScriptParser.FactorContext):
        if ctx.getChildCount() == 2 and ctx.getChild(0).getText() == '!':
            # factor: '!' factor
            return {
                'operator': '!',
                'operands': [
                    self.visitFactor(ctx.factor()),
                ],
            }
        elif ctx.getChildCount() == 3 and ctx.getChild(0).getText() == '(' and ctx.getChild(2).getText() == ')':
            # factor: '(' expr ')'
            return self.visitExpr(ctx.expr())

        else:
            # factor: predicate
            return self.visitPredicate(ctx.predicate())

    # Visit a parse tree produced by EveScriptParser#predicate.
    def visitPredicate(self, ctx: EveScriptParser.PredicateContext):
        return {
            'operator': self.visitOperator(ctx.operator()),
            'operands': [self.visitOperand(operand) for operand in ctx.operand()],
        }

    # Visit a parse tree produced by EveScriptParser#operator.
    def visitOperator(self, ctx: EveScriptParser.OperatorContext):
        text = ctx.getChild(0).getText()
        return text

    # Visit a parse tree produced by EveScriptParser#operand.
    def visitOperand(self, ctx: EveScriptParser.OperandContext):
        const = ctx.const()
        if const is not None:
            return self.visitConst(ctx.const())
        else:
            return ctx.getText()

    # Visit a parse tree produced by EveScriptParser#const.
    def visitConst(self, ctx: EveScriptParser.ConstContext):
        text = ctx.getText()
        if ctx.STRING():
            return text.strip('"')
        elif ctx.NUMBER():
            if '.' in text:
                return float(text)
            else:
                return int(text)
        elif text == 'true':
            return True
        else:
            # text == 'false'
            return False

    # Visit a parse tree produced by EveScriptParser#action.
    def visitAction(self, ctx: EveScriptParser.ActionContext):
        return {
            'func': ctx.KEYWORD().getText(),
            'params': [self.visitParam(param) for param in ctx.param()],
        }

    # Visit a parse tree produced by EveScriptParser#param.
    def visitParam(self, ctx: EveScriptParser.ParamContext):
        return self.visitConst(ctx.const())
