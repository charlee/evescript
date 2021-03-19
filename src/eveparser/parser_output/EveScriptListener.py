# Generated from EveScript.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .EveScriptParser import EveScriptParser
else:
    from EveScriptParser import EveScriptParser

# This class defines a complete listener for a parse tree produced by EveScriptParser.
class EveScriptListener(ParseTreeListener):

    # Enter a parse tree produced by EveScriptParser#script.
    def enterScript(self, ctx:EveScriptParser.ScriptContext):
        pass

    # Exit a parse tree produced by EveScriptParser#script.
    def exitScript(self, ctx:EveScriptParser.ScriptContext):
        pass


    # Enter a parse tree produced by EveScriptParser#trigger.
    def enterTrigger(self, ctx:EveScriptParser.TriggerContext):
        pass

    # Exit a parse tree produced by EveScriptParser#trigger.
    def exitTrigger(self, ctx:EveScriptParser.TriggerContext):
        pass


    # Enter a parse tree produced by EveScriptParser#event.
    def enterEvent(self, ctx:EveScriptParser.EventContext):
        pass

    # Exit a parse tree produced by EveScriptParser#event.
    def exitEvent(self, ctx:EveScriptParser.EventContext):
        pass


    # Enter a parse tree produced by EveScriptParser#condition.
    def enterCondition(self, ctx:EveScriptParser.ConditionContext):
        pass

    # Exit a parse tree produced by EveScriptParser#condition.
    def exitCondition(self, ctx:EveScriptParser.ConditionContext):
        pass


    # Enter a parse tree produced by EveScriptParser#expr.
    def enterExpr(self, ctx:EveScriptParser.ExprContext):
        pass

    # Exit a parse tree produced by EveScriptParser#expr.
    def exitExpr(self, ctx:EveScriptParser.ExprContext):
        pass


    # Enter a parse tree produced by EveScriptParser#term.
    def enterTerm(self, ctx:EveScriptParser.TermContext):
        pass

    # Exit a parse tree produced by EveScriptParser#term.
    def exitTerm(self, ctx:EveScriptParser.TermContext):
        pass


    # Enter a parse tree produced by EveScriptParser#factor.
    def enterFactor(self, ctx:EveScriptParser.FactorContext):
        pass

    # Exit a parse tree produced by EveScriptParser#factor.
    def exitFactor(self, ctx:EveScriptParser.FactorContext):
        pass


    # Enter a parse tree produced by EveScriptParser#predicate.
    def enterPredicate(self, ctx:EveScriptParser.PredicateContext):
        pass

    # Exit a parse tree produced by EveScriptParser#predicate.
    def exitPredicate(self, ctx:EveScriptParser.PredicateContext):
        pass


    # Enter a parse tree produced by EveScriptParser#operator.
    def enterOperator(self, ctx:EveScriptParser.OperatorContext):
        pass

    # Exit a parse tree produced by EveScriptParser#operator.
    def exitOperator(self, ctx:EveScriptParser.OperatorContext):
        pass


    # Enter a parse tree produced by EveScriptParser#operand.
    def enterOperand(self, ctx:EveScriptParser.OperandContext):
        pass

    # Exit a parse tree produced by EveScriptParser#operand.
    def exitOperand(self, ctx:EveScriptParser.OperandContext):
        pass


    # Enter a parse tree produced by EveScriptParser#const.
    def enterConst(self, ctx:EveScriptParser.ConstContext):
        pass

    # Exit a parse tree produced by EveScriptParser#const.
    def exitConst(self, ctx:EveScriptParser.ConstContext):
        pass


    # Enter a parse tree produced by EveScriptParser#action.
    def enterAction(self, ctx:EveScriptParser.ActionContext):
        pass

    # Exit a parse tree produced by EveScriptParser#action.
    def exitAction(self, ctx:EveScriptParser.ActionContext):
        pass


    # Enter a parse tree produced by EveScriptParser#param.
    def enterParam(self, ctx:EveScriptParser.ParamContext):
        pass

    # Exit a parse tree produced by EveScriptParser#param.
    def exitParam(self, ctx:EveScriptParser.ParamContext):
        pass



del EveScriptParser