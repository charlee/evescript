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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\30")
        buf.write("p\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16\t")
        buf.write("\16\3\2\7\2\36\n\2\f\2\16\2!\13\2\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\7\3)\n\3\f\3\16\3,\13\3\3\3\3\3\3\4\3\4\3\5\3\5\3")
        buf.write("\5\3\5\3\5\3\5\7\58\n\5\f\5\16\5;\13\5\3\5\3\5\3\6\3\6")
        buf.write("\3\6\3\6\3\6\5\6D\n\6\3\7\3\7\3\7\3\7\3\7\5\7K\n\7\3\b")
        buf.write("\3\b\3\b\3\b\3\b\3\b\3\b\5\bT\n\b\3\t\3\t\3\t\3\t\3\n")
        buf.write("\3\n\3\13\3\13\5\13^\n\13\3\f\3\f\3\r\3\r\3\r\3\r\3\r")
        buf.write("\7\rg\n\r\f\r\16\rj\13\r\3\r\3\r\3\16\3\16\3\16\2\2\17")
        buf.write("\2\4\6\b\n\f\16\20\22\24\26\30\32\2\4\4\2\f\21\23\23\4")
        buf.write("\2\24\24\26\27\2k\2\37\3\2\2\2\4\"\3\2\2\2\6/\3\2\2\2")
        buf.write("\b\61\3\2\2\2\nC\3\2\2\2\fJ\3\2\2\2\16S\3\2\2\2\20U\3")
        buf.write("\2\2\2\22Y\3\2\2\2\24]\3\2\2\2\26_\3\2\2\2\30a\3\2\2\2")
        buf.write("\32m\3\2\2\2\34\36\5\4\3\2\35\34\3\2\2\2\36!\3\2\2\2\37")
        buf.write("\35\3\2\2\2\37 \3\2\2\2 \3\3\2\2\2!\37\3\2\2\2\"#\7\3")
        buf.write("\2\2#$\7\4\2\2$%\5\6\4\2%&\7\5\2\2&*\7\6\2\2\')\5\b\5")
        buf.write("\2(\'\3\2\2\2),\3\2\2\2*(\3\2\2\2*+\3\2\2\2+-\3\2\2\2")
        buf.write(",*\3\2\2\2-.\7\7\2\2.\5\3\2\2\2/\60\7\23\2\2\60\7\3\2")
        buf.write("\2\2\61\62\7\b\2\2\62\63\7\4\2\2\63\64\5\n\6\2\64\65\7")
        buf.write("\5\2\2\659\7\6\2\2\668\5\30\r\2\67\66\3\2\2\28;\3\2\2")
        buf.write("\29\67\3\2\2\29:\3\2\2\2:<\3\2\2\2;9\3\2\2\2<=\7\7\2\2")
        buf.write("=\t\3\2\2\2>?\5\f\7\2?@\7\t\2\2@A\5\n\6\2AD\3\2\2\2BD")
        buf.write("\5\f\7\2C>\3\2\2\2CB\3\2\2\2D\13\3\2\2\2EF\5\16\b\2FG")
        buf.write("\7\n\2\2GH\5\f\7\2HK\3\2\2\2IK\5\16\b\2JE\3\2\2\2JI\3")
        buf.write("\2\2\2K\r\3\2\2\2LM\7\4\2\2MN\5\n\6\2NO\7\5\2\2OT\3\2")
        buf.write("\2\2PQ\7\13\2\2QT\5\16\b\2RT\5\20\t\2SL\3\2\2\2SP\3\2")
        buf.write("\2\2SR\3\2\2\2T\17\3\2\2\2UV\5\24\13\2VW\5\22\n\2WX\5")
        buf.write("\24\13\2X\21\3\2\2\2YZ\t\2\2\2Z\23\3\2\2\2[^\7\25\2\2")
        buf.write("\\^\5\26\f\2][\3\2\2\2]\\\3\2\2\2^\25\3\2\2\2_`\t\3\2")
        buf.write("\2`\27\3\2\2\2ab\7\23\2\2bc\7\4\2\2ch\5\32\16\2de\7\22")
        buf.write("\2\2eg\5\32\16\2fd\3\2\2\2gj\3\2\2\2hf\3\2\2\2hi\3\2\2")
        buf.write("\2ik\3\2\2\2jh\3\2\2\2kl\7\5\2\2l\31\3\2\2\2mn\5\24\13")
        buf.write("\2n\33\3\2\2\2\n\37*9CJS]h")
        return buf.getvalue()


class EveScriptParser ( Parser ):

    grammarFileName = "EveScript.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'on'", "'('", "')'", "'{'", "'}'", "'if'", 
                     "'||'", "'&&'", "'!'", "'>'", "'>='", "'<'", "'<='", 
                     "'=='", "'!='", "','" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "KEYWORD", "STRING", "VARIABLE", "NUMBER", 
                      "BOOL", "WS" ]

    RULE_script = 0
    RULE_trigger = 1
    RULE_event = 2
    RULE_condition = 3
    RULE_expr = 4
    RULE_term = 5
    RULE_factor = 6
    RULE_predicate = 7
    RULE_operator = 8
    RULE_operand = 9
    RULE_const = 10
    RULE_action = 11
    RULE_param = 12

    ruleNames =  [ "script", "trigger", "event", "condition", "expr", "term", 
                   "factor", "predicate", "operator", "operand", "const", 
                   "action", "param" ]

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
    KEYWORD=17
    STRING=18
    VARIABLE=19
    NUMBER=20
    BOOL=21
    WS=22

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

        def trigger(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EveScriptParser.TriggerContext)
            else:
                return self.getTypedRuleContext(EveScriptParser.TriggerContext,i)


        def getRuleIndex(self):
            return EveScriptParser.RULE_script

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitScript" ):
                return visitor.visitScript(self)
            else:
                return visitor.visitChildren(self)




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
                self.trigger()
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


    class TriggerContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def event(self):
            return self.getTypedRuleContext(EveScriptParser.EventContext,0)


        def condition(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EveScriptParser.ConditionContext)
            else:
                return self.getTypedRuleContext(EveScriptParser.ConditionContext,i)


        def getRuleIndex(self):
            return EveScriptParser.RULE_trigger

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTrigger" ):
                return visitor.visitTrigger(self)
            else:
                return visitor.visitChildren(self)




    def trigger(self):

        localctx = EveScriptParser.TriggerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_trigger)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 32
            self.match(EveScriptParser.T__0)
            self.state = 33
            self.match(EveScriptParser.T__1)
            self.state = 34
            self.event()
            self.state = 35
            self.match(EveScriptParser.T__2)
            self.state = 36
            self.match(EveScriptParser.T__3)
            self.state = 40
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==EveScriptParser.T__5:
                self.state = 37
                self.condition()
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


    class EventContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KEYWORD(self):
            return self.getToken(EveScriptParser.KEYWORD, 0)

        def getRuleIndex(self):
            return EveScriptParser.RULE_event

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEvent" ):
                return visitor.visitEvent(self)
            else:
                return visitor.visitChildren(self)




    def event(self):

        localctx = EveScriptParser.EventContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_event)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 45
            self.match(EveScriptParser.KEYWORD)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionContext(ParserRuleContext):
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
            return EveScriptParser.RULE_condition

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondition" ):
                return visitor.visitCondition(self)
            else:
                return visitor.visitChildren(self)




    def condition(self):

        localctx = EveScriptParser.ConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_condition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 47
            self.match(EveScriptParser.T__5)
            self.state = 48
            self.match(EveScriptParser.T__1)
            self.state = 49
            self.expr()
            self.state = 50
            self.match(EveScriptParser.T__2)
            self.state = 51
            self.match(EveScriptParser.T__3)
            self.state = 55
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==EveScriptParser.KEYWORD:
                self.state = 52
                self.action()
                self.state = 57
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 58
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = EveScriptParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_expr)
        try:
            self.state = 65
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 60
                self.term()
                self.state = 61
                self.match(EveScriptParser.T__6)
                self.state = 62
                self.expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 64
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm" ):
                return visitor.visitTerm(self)
            else:
                return visitor.visitChildren(self)




    def term(self):

        localctx = EveScriptParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_term)
        try:
            self.state = 72
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 67
                self.factor()
                self.state = 68
                self.match(EveScriptParser.T__7)
                self.state = 69
                self.term()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 71
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFactor" ):
                return visitor.visitFactor(self)
            else:
                return visitor.visitChildren(self)




    def factor(self):

        localctx = EveScriptParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_factor)
        try:
            self.state = 81
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [EveScriptParser.T__1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 74
                self.match(EveScriptParser.T__1)
                self.state = 75
                self.expr()
                self.state = 76
                self.match(EveScriptParser.T__2)
                pass
            elif token in [EveScriptParser.T__8]:
                self.enterOuterAlt(localctx, 2)
                self.state = 78
                self.match(EveScriptParser.T__8)
                self.state = 79
                self.factor()
                pass
            elif token in [EveScriptParser.STRING, EveScriptParser.VARIABLE, EveScriptParser.NUMBER, EveScriptParser.BOOL]:
                self.enterOuterAlt(localctx, 3)
                self.state = 80
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPredicate" ):
                return visitor.visitPredicate(self)
            else:
                return visitor.visitChildren(self)




    def predicate(self):

        localctx = EveScriptParser.PredicateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_predicate)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 83
            self.operand()
            self.state = 84
            self.operator()
            self.state = 85
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperator" ):
                return visitor.visitOperator(self)
            else:
                return visitor.visitChildren(self)




    def operator(self):

        localctx = EveScriptParser.OperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_operator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 87
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << EveScriptParser.T__9) | (1 << EveScriptParser.T__10) | (1 << EveScriptParser.T__11) | (1 << EveScriptParser.T__12) | (1 << EveScriptParser.T__13) | (1 << EveScriptParser.T__14) | (1 << EveScriptParser.KEYWORD))) != 0)):
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperand" ):
                return visitor.visitOperand(self)
            else:
                return visitor.visitChildren(self)




    def operand(self):

        localctx = EveScriptParser.OperandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_operand)
        try:
            self.state = 91
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [EveScriptParser.VARIABLE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 89
                self.match(EveScriptParser.VARIABLE)
                pass
            elif token in [EveScriptParser.STRING, EveScriptParser.NUMBER, EveScriptParser.BOOL]:
                self.enterOuterAlt(localctx, 2)
                self.state = 90
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

        def BOOL(self):
            return self.getToken(EveScriptParser.BOOL, 0)

        def getRuleIndex(self):
            return EveScriptParser.RULE_const

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConst" ):
                return visitor.visitConst(self)
            else:
                return visitor.visitChildren(self)




    def const(self):

        localctx = EveScriptParser.ConstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_const)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 93
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << EveScriptParser.STRING) | (1 << EveScriptParser.NUMBER) | (1 << EveScriptParser.BOOL))) != 0)):
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAction" ):
                return visitor.visitAction(self)
            else:
                return visitor.visitChildren(self)




    def action(self):

        localctx = EveScriptParser.ActionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_action)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 95
            self.match(EveScriptParser.KEYWORD)
            self.state = 96
            self.match(EveScriptParser.T__1)
            self.state = 97
            self.param()
            self.state = 102
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==EveScriptParser.T__15:
                self.state = 98
                self.match(EveScriptParser.T__15)
                self.state = 99
                self.param()
                self.state = 104
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 105
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

        def operand(self):
            return self.getTypedRuleContext(EveScriptParser.OperandContext,0)


        def getRuleIndex(self):
            return EveScriptParser.RULE_param

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam" ):
                return visitor.visitParam(self)
            else:
                return visitor.visitChildren(self)




    def param(self):

        localctx = EveScriptParser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 107
            self.operand()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





