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
        buf.write("]\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\3\2\7\2\32\n\2")
        buf.write("\f\2\16\2\35\13\2\3\3\3\3\3\3\3\3\3\3\3\3\7\3%\n\3\f\3")
        buf.write("\16\3(\13\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\5\4\61\n\4\3\5")
        buf.write("\3\5\3\5\3\5\3\5\5\58\n\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6")
        buf.write("\5\6A\n\6\3\7\3\7\3\7\3\7\3\b\3\b\3\t\3\t\5\tK\n\t\3\n")
        buf.write("\3\n\3\13\3\13\3\13\3\13\3\13\7\13T\n\13\f\13\16\13W\13")
        buf.write("\13\3\13\3\13\3\f\3\f\3\f\2\2\r\2\4\6\b\n\f\16\20\22\24")
        buf.write("\26\2\4\4\2\13\20\24\24\5\2\21\22\25\25\27\27\2Y\2\33")
        buf.write("\3\2\2\2\4\36\3\2\2\2\6\60\3\2\2\2\b\67\3\2\2\2\n@\3\2")
        buf.write("\2\2\fB\3\2\2\2\16F\3\2\2\2\20J\3\2\2\2\22L\3\2\2\2\24")
        buf.write("N\3\2\2\2\26Z\3\2\2\2\30\32\5\4\3\2\31\30\3\2\2\2\32\35")
        buf.write("\3\2\2\2\33\31\3\2\2\2\33\34\3\2\2\2\34\3\3\2\2\2\35\33")
        buf.write("\3\2\2\2\36\37\7\3\2\2\37 \7\4\2\2 !\5\6\4\2!\"\7\5\2")
        buf.write("\2\"&\7\6\2\2#%\5\24\13\2$#\3\2\2\2%(\3\2\2\2&$\3\2\2")
        buf.write("\2&\'\3\2\2\2\')\3\2\2\2(&\3\2\2\2)*\7\7\2\2*\5\3\2\2")
        buf.write("\2+,\5\b\5\2,-\7\b\2\2-.\5\6\4\2.\61\3\2\2\2/\61\5\b\5")
        buf.write("\2\60+\3\2\2\2\60/\3\2\2\2\61\7\3\2\2\2\62\63\5\n\6\2")
        buf.write("\63\64\7\t\2\2\64\65\5\b\5\2\658\3\2\2\2\668\5\n\6\2\67")
        buf.write("\62\3\2\2\2\67\66\3\2\2\28\t\3\2\2\29:\7\4\2\2:;\5\6\4")
        buf.write("\2;<\7\5\2\2<A\3\2\2\2=>\7\n\2\2>A\5\n\6\2?A\5\f\7\2@")
        buf.write("9\3\2\2\2@=\3\2\2\2@?\3\2\2\2A\13\3\2\2\2BC\5\20\t\2C")
        buf.write("D\5\16\b\2DE\5\20\t\2E\r\3\2\2\2FG\t\2\2\2G\17\3\2\2\2")
        buf.write("HK\7\26\2\2IK\5\22\n\2JH\3\2\2\2JI\3\2\2\2K\21\3\2\2\2")
        buf.write("LM\t\3\2\2M\23\3\2\2\2NO\7\24\2\2OP\7\4\2\2PU\5\26\f\2")
        buf.write("QR\7\23\2\2RT\5\26\f\2SQ\3\2\2\2TW\3\2\2\2US\3\2\2\2U")
        buf.write("V\3\2\2\2VX\3\2\2\2WU\3\2\2\2XY\7\5\2\2Y\25\3\2\2\2Z[")
        buf.write("\5\22\n\2[\27\3\2\2\2\t\33&\60\67@JU")
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
    RULE_const = 8
    RULE_action = 9
    RULE_param = 10

    ruleNames =  [ "script", "statement", "expr", "term", "factor", "predicate", 
                   "operator", "operand", "const", "action", "param" ]

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
            self.state = 25
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==EveScriptParser.T__0:
                self.state = 22
                self.statement()
                self.state = 27
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
            self.state = 28
            self.match(EveScriptParser.T__0)
            self.state = 29
            self.match(EveScriptParser.T__1)
            self.state = 30
            self.expr()
            self.state = 31
            self.match(EveScriptParser.T__2)
            self.state = 32
            self.match(EveScriptParser.T__3)
            self.state = 36
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==EveScriptParser.KEYWORD:
                self.state = 33
                self.action()
                self.state = 38
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 39
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
            self.state = 46
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 41
                self.term()
                self.state = 42
                self.match(EveScriptParser.T__5)
                self.state = 43
                self.expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 45
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
            self.state = 53
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 48
                self.factor()
                self.state = 49
                self.match(EveScriptParser.T__6)
                self.state = 50
                self.term()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 52
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
            self.state = 62
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [EveScriptParser.T__1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 55
                self.match(EveScriptParser.T__1)
                self.state = 56
                self.expr()
                self.state = 57
                self.match(EveScriptParser.T__2)
                pass
            elif token in [EveScriptParser.T__7]:
                self.enterOuterAlt(localctx, 2)
                self.state = 59
                self.match(EveScriptParser.T__7)
                self.state = 60
                self.factor()
                pass
            elif token in [EveScriptParser.T__14, EveScriptParser.T__15, EveScriptParser.STRING, EveScriptParser.VARIABLE, EveScriptParser.NUMBER]:
                self.enterOuterAlt(localctx, 3)
                self.state = 61
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


        def getRuleIndex(self):
            return EveScriptParser.RULE_predicate




    def predicate(self):

        localctx = EveScriptParser.PredicateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_predicate)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 64
            self.operand()
            self.state = 65
            self.operator()
            self.state = 66
            self.operand()
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
            self.state = 68
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
            self.state = 72
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [EveScriptParser.VARIABLE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 70
                self.match(EveScriptParser.VARIABLE)
                pass
            elif token in [EveScriptParser.T__14, EveScriptParser.T__15, EveScriptParser.STRING, EveScriptParser.NUMBER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 71
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


    class ConstContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(EveScriptParser.STRING, 0)

        def NUMBER(self):
            return self.getToken(EveScriptParser.NUMBER, 0)

        def getRuleIndex(self):
            return EveScriptParser.RULE_const




    def const(self):

        localctx = EveScriptParser.ConstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_const)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 74
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << EveScriptParser.T__14) | (1 << EveScriptParser.T__15) | (1 << EveScriptParser.STRING) | (1 << EveScriptParser.NUMBER))) != 0)):
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


    class ActionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KEYWORD(self):
            return self.getToken(EveScriptParser.KEYWORD, 0)

        def param(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EveScriptParser.ParamContext)
            else:
                return self.getTypedRuleContext(EveScriptParser.ParamContext,i)


        def getRuleIndex(self):
            return EveScriptParser.RULE_action




    def action(self):

        localctx = EveScriptParser.ActionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_action)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 76
            self.match(EveScriptParser.KEYWORD)
            self.state = 77
            self.match(EveScriptParser.T__1)
            self.state = 78
            self.param()
            self.state = 83
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==EveScriptParser.T__16:
                self.state = 79
                self.match(EveScriptParser.T__16)
                self.state = 80
                self.param()
                self.state = 85
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 86
            self.match(EveScriptParser.T__2)
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
        self.enterRule(localctx, 20, self.RULE_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 88
            self.const()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





