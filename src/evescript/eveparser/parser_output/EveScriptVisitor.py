# Generated from EveScript.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .EveScriptParser import EveScriptParser
else:
    from EveScriptParser import EveScriptParser

# This class defines a complete generic visitor for a parse tree produced by EveScriptParser.

class EveScriptVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by EveScriptParser#script.
    def visitScript(self, ctx:EveScriptParser.ScriptContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EveScriptParser#trigger.
    def visitTrigger(self, ctx:EveScriptParser.TriggerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EveScriptParser#event.
    def visitEvent(self, ctx:EveScriptParser.EventContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EveScriptParser#condition.
    def visitCondition(self, ctx:EveScriptParser.ConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EveScriptParser#expr.
    def visitExpr(self, ctx:EveScriptParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EveScriptParser#term.
    def visitTerm(self, ctx:EveScriptParser.TermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EveScriptParser#factor.
    def visitFactor(self, ctx:EveScriptParser.FactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EveScriptParser#predicate.
    def visitPredicate(self, ctx:EveScriptParser.PredicateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EveScriptParser#operator.
    def visitOperator(self, ctx:EveScriptParser.OperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EveScriptParser#operand.
    def visitOperand(self, ctx:EveScriptParser.OperandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EveScriptParser#const.
    def visitConst(self, ctx:EveScriptParser.ConstContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EveScriptParser#action.
    def visitAction(self, ctx:EveScriptParser.ActionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EveScriptParser#param.
    def visitParam(self, ctx:EveScriptParser.ParamContext):
        return self.visitChildren(ctx)



del EveScriptParser