# Generated from EveScript.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\31")
        buf.write("m\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16\t")
        buf.write("\16\3\2\7\2\36\n\2\f\2\16\2!\13\2\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\7\3)\n\3\f\3\16\3,\13\3\3\3\3\3\3\4\3\4\3\4\3\4\3")
        buf.write("\4\5\4\65\n\4\3\5\3\5\3\5\3\5\3\5\5\5<\n\5\3\6\3\6\3\6")
        buf.write("\3\6\3\6\3\6\3\6\5\6E\n\6\3\7\3\7\3\7\3\7\3\7\5\7L\n\7")
        buf.write("\3\b\3\b\3\t\3\t\5\tR\n\t\3\n\3\n\3\13\3\13\3\13\5\13")
        buf.write("Y\n\13\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\7\rc\n\r\f\r\16")
        buf.write("\rf\13\r\3\r\5\ri\n\r\3\16\3\16\3\16\2\2\17\2\4\6\b\n")
        buf.write("\f\16\20\22\24\26\30\32\2\4\4\2\13\20\24\24\3\2\21\22")
        buf.write("\2k\2\37\3\2\2\2\4\"\3\2\2\2\6\64\3\2\2\2\b;\3\2\2\2\n")
        buf.write("D\3\2\2\2\fK\3\2\2\2\16M\3\2\2\2\20Q\3\2\2\2\22S\3\2\2")
        buf.write("\2\24X\3\2\2\2\26Z\3\2\2\2\30h\3\2\2\2\32j\3\2\2\2\34")
        buf.write("\36\5\4\3\2\35\34\3\2\2\2\36!\3\2\2\2\37\35\3\2\2\2\37")
        buf.write(" \3\2\2\2 \3\3\2\2\2!\37\3\2\2\2\"#\7\3\2\2#$\7\4\2\2")
        buf.write("$%\5\6\4\2%&\7\5\2\2&*\7\6\2\2\')\5\26\f\2(\'\3\2\2\2")
        buf.write("),\3\2\2\2*(\3\2\2\2*+\3\2\2\2+-\3\2\2\2,*\3\2\2\2-.\7")
        buf.write("\7\2\2.\5\3\2\2\2/\60\5\b\5\2\60\61\7\b\2\2\61\62\5\6")
        buf.write("\4\2\62\65\3\2\2\2\63\65\5\b\5\2\64/\3\2\2\2\64\63\3\2")
        buf.write("\2\2\65\7\3\2\2\2\66\67\5\n\6\2\678\7\t\2\289\5\b\5\2")
        buf.write("9<\3\2\2\2:<\5\n\6\2;\66\3\2\2\2;:\3\2\2\2<\t\3\2\2\2")
        buf.write("=>\7\4\2\2>?\5\6\4\2?@\7\5\2\2@E\3\2\2\2AB\7\n\2\2BE\5")
        buf.write("\n\6\2CE\5\f\7\2D=\3\2\2\2DA\3\2\2\2DC\3\2\2\2E\13\3\2")
        buf.write("\2\2FG\5\20\t\2GH\5\16\b\2HI\5\20\t\2IL\3\2\2\2JL\5\22")
        buf.write("\n\2KF\3\2\2\2KJ\3\2\2\2L\r\3\2\2\2MN\t\2\2\2N\17\3\2")
        buf.write("\2\2OR\7\26\2\2PR\5\24\13\2QO\3\2\2\2QP\3\2\2\2R\21\3")
        buf.write("\2\2\2ST\t\3\2\2T\23\3\2\2\2UY\7\25\2\2VY\7\27\2\2WY\5")
        buf.write("\22\n\2XU\3\2\2\2XV\3\2\2\2XW\3\2\2\2Y\25\3\2\2\2Z[\7")
        buf.write("\24\2\2[\\\7\4\2\2\\]\5\30\r\2]^\7\5\2\2^\27\3\2\2\2_")
        buf.write("d\5\32\16\2`a\7\23\2\2ac\5\32\16\2b`\3\2\2\2cf\3\2\2\2")
        buf.write("db\3\2\2\2de\3\2\2\2ei\3\2\2\2fd\3\2\2\2gi\3\2\2\2h_\3")
        buf.write("\2\2\2hg\3\2\2\2i\31\3\2\2\2jk\5\24\13\2k\33\3\2\2\2\f")
        buf.write("\37*\64;DKQXdh")
        return buf.getvalue()


class EveScriptParser ( Parser ):

    grammarFileName = "EveScript.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'if'", "'('", "')'", "'{'", "'}'", "'||'", 
                     "'&&'", "'!'", "'>'", "'>='", "'<'", "'<='", "'=='", 
                     "'!='", "'true'", "'false'", "','" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "KEYWORD", "STRING", "VARIABLE", 
                      "NUMBER", "COMMENT", "WS" ]

    RULE_script = 0
    RULE_statement = 1
    RULE_expr = 2
    RULE_term = 3
    RULE_factor = 4
    RULE_predicate = 5
    RULE_operator = 6
    RULE_operand = 7
    RULE_boolean = 8
    RULE_const = 9
    RULE_action = 10
    RULE_params = 11
    RULE_param = 12

    ruleNames =  [ "script", "statement", "expr", "term", "factor", "predicate", 
                   "operator", "operand", "boolean", "const", "action", 
                   "params", "param" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    KEYWORD=18
    STRING=19
    VARIABLE=20
    NUMBER=21
    COMMENT=22
    WS=23

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ScriptContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EveScriptParser.StatementContext)
            else:
                return self.getTypedRuleContext(EveScriptParser.StatementContext,i)


        def getRuleIndex(self):
            return EveScriptParser.RULE_script




    def script(self):

        localctx = EveScriptParser.ScriptContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_script)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 29
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==EveScriptParser.T__0:
                self.state = 26
                self.statement()
                self.state = 31
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(EveScriptParser.ExprContext,0)


        def action(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EveScriptParser.ActionContext)
            else:
                return self.getTypedRuleContext(EveScriptParser.ActionContext,i)


        def getRuleIndex(self):
            return EveScriptParser.RULE_statement




    def statement(self):

        localctx = EveScriptParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 32
            self.match(EveScriptParser.T__0)
            self.state = 33
            self.match(EveScriptParser.T__1)
            self.state = 34
            self.expr()
            self.state = 35
            self.match(EveScriptParser.T__2)
            self.state = 36
            self.match(EveScriptParser.T__3)
            self.state = 40
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==EveScriptParser.KEYWORD:
                self.state = 37
                self.action()
                self.state = 42
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 43
            self.match(EveScriptParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term(self):
            return self.getTypedRuleContext(EveScriptParser.TermContext,0)


        def expr(self):
            return self.getTypedRuleContext(EveScriptParser.ExprContext,0)


        def getRuleIndex(self):
            return EveScriptParser.RULE_expr




    def expr(self):

        localctx = EveScriptParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_expr)
        try:
            self.state = 50
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 45
                self.term()
                self.state = 46
                self.match(EveScriptParser.T__5)
                self.state = 47
                self.expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 49
                self.term()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def factor(self):
            return self.getTypedRuleContext(EveScriptParser.FactorContext,0)


        def term(self):
            return self.getTypedRuleContext(EveScriptParser.TermContext,0)


        def getRuleIndex(self):
            return EveScriptParser.RULE_term




    def term(self):

        localctx = EveScriptParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_term)
        try:
            self.state = 57
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 52
                self.factor()
                self.state = 53
                self.match(EveScriptParser.T__6)
                self.state = 54
                self.term()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 56
                self.factor()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FactorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(EveScriptParser.ExprContext,0)


        def factor(self):
            return self.getTypedRuleContext(EveScriptParser.FactorContext,0)


        def predicate(self):
            return self.getTypedRuleContext(EveScriptParser.PredicateContext,0)


        def getRuleIndex(self):
            return EveScriptParser.RULE_factor




    def factor(self):

        localctx = EveScriptParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_factor)
        try:
            self.state = 66
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [EveScriptParser.T__1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 59
                self.match(EveScriptParser.T__1)
                self.state = 60
                self.expr()
                self.state = 61
                self.match(EveScriptParser.T__2)
                pass
            elif token in [EveScriptParser.T__7]:
                self.enterOuterAlt(localctx, 2)
                self.state = 63
                self.match(EveScriptParser.T__7)
                self.state = 64
                self.factor()
                pass
            elif token in [EveScriptParser.T__14, EveScriptParser.T__15, EveScriptParser.STRING, EveScriptParser.VARIABLE, EveScriptParser.NUMBER]:
                self.enterOuterAlt(localctx, 3)
                self.state = 65
                self.predicate()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PredicateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def operand(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EveScriptParser.OperandContext)
            else:
                return self.getTypedRuleContext(EveScriptParser.OperandContext,i)


        def operator(self):
            return self.getTypedRuleContext(EveScriptParser.OperatorContext,0)


        def boolean(self):
            return self.getTypedRuleContext(EveScriptParser.BooleanContext,0)


        def getRuleIndex(self):
            return EveScriptParser.RULE_predicate




    def predicate(self):

        localctx = EveScriptParser.PredicateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_predicate)
        try:
            self.state = 73
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 68
                self.operand()
                self.state = 69
                self.operator()
                self.state = 70
                self.operand()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 72
                self.boolean()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KEYWORD(self):
            return self.getToken(EveScriptParser.KEYWORD, 0)

        def getRuleIndex(self):
            return EveScriptParser.RULE_operator




    def operator(self):

        localctx = EveScriptParser.OperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_operator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 75
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << EveScriptParser.T__8) | (1 << EveScriptParser.T__9) | (1 << EveScriptParser.T__10) | (1 << EveScriptParser.T__11) | (1 << EveScriptParser.T__12) | (1 << EveScriptParser.T__13) | (1 << EveScriptParser.KEYWORD))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VARIABLE(self):
            return self.getToken(EveScriptParser.VARIABLE, 0)

        def const(self):
            return self.getTypedRuleContext(EveScriptParser.ConstContext,0)


        def getRuleIndex(self):
            return EveScriptParser.RULE_operand




    def operand(self):

        localctx = EveScriptParser.OperandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_operand)
        try:
            self.state = 79
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [EveScriptParser.VARIABLE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 77
                self.match(EveScriptParser.VARIABLE)
                pass
            elif token in [EveScriptParser.T__14, EveScriptParser.T__15, EveScriptParser.STRING, EveScriptParser.NUMBER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 78
                self.const()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BooleanContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EveScriptParser.RULE_boolean




    def boolean(self):

        localctx = EveScriptParser.BooleanContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_boolean)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 81
            _la = self._input.LA(1)
            if not(_la==EveScriptParser.T__14 or _la==EveScriptParser.T__15):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(EveScriptParser.STRING, 0)

        def NUMBER(self):
            return self.getToken(EveScriptParser.NUMBER, 0)

        def boolean(self):
            return self.getTypedRuleContext(EveScriptParser.BooleanContext,0)


        def getRuleIndex(self):
            return EveScriptParser.RULE_const




    def const(self):

        localctx = EveScriptParser.ConstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_const)
        try:
            self.state = 86
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [EveScriptParser.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 83
                self.match(EveScriptParser.STRING)
                pass
            elif token in [EveScriptParser.NUMBER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 84
                self.match(EveScriptParser.NUMBER)
                pass
            elif token in [EveScriptParser.T__14, EveScriptParser.T__15]:
                self.enterOuterAlt(localctx, 3)
                self.state = 85
                self.boolean()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ActionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KEYWORD(self):
            return self.getToken(EveScriptParser.KEYWORD, 0)

        def params(self):
            return self.getTypedRuleContext(EveScriptParser.ParamsContext,0)


        def getRuleIndex(self):
            return EveScriptParser.RULE_action




    def action(self):

        localctx = EveScriptParser.ActionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_action)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 88
            self.match(EveScriptParser.KEYWORD)
            self.state = 89
            self.match(EveScriptParser.T__1)
            self.state = 90
            self.params()
            self.state = 91
            self.match(EveScriptParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EveScriptParser.ParamContext)
            else:
                return self.getTypedRuleContext(EveScriptParser.ParamContext,i)


        def getRuleIndex(self):
            return EveScriptParser.RULE_params




    def params(self):

        localctx = EveScriptParser.ParamsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_params)
        self._la = 0 # Token type
        try:
            self.state = 102
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [EveScriptParser.T__14, EveScriptParser.T__15, EveScriptParser.STRING, EveScriptParser.NUMBER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 93
                self.param()
                self.state = 98
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==EveScriptParser.T__16:
                    self.state = 94
                    self.match(EveScriptParser.T__16)
                    self.state = 95
                    self.param()
                    self.state = 100
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            elif token in [EveScriptParser.T__2]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def const(self):
            return self.getTypedRuleContext(EveScriptParser.ConstContext,0)


        def getRuleIndex(self):
            return EveScriptParser.RULE_param




    def param(self):

        localctx = EveScriptParser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 104
            self.const()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





