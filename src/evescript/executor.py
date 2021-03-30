import logging
import sys
from copy import copy

from .exceptions import InvalidAction, InvalidActionParams, InvalidOperator, InvalidVariable

logger = logging.getLogger(__name__)
handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.DEBUG)
logger.addHandler(handler)

logger.setLevel(logging.INFO)

DEFAULT_OPERATORS = {
    # Logical operators
    '&&': lambda a, b: a and b,
    '||': lambda a, b: a or b,
    '!': lambda a: not a,

    # Comparison operatos
    '<': lambda a, b: a < b,
    '<=': lambda a, b: a <= b,
    '>': lambda a, b: a > b,
    '>=': lambda a, b: a >= b,
    '==': lambda a, b: a == b,
    '!=': lambda a, b: a != b,
}


class EveScriptExecutor:

    def __init__(self, config={}):
        self.actions = {}
        self.variables = {}
        self.operators = copy(DEFAULT_OPERATORS)

        self.add_actions(config.get('actions', {}))
        self.add_variables(config.get('variables', {}))
        self.add_operators(config.get('operators', {}))

    def add_actions(self, actions):
        self.actions.update(actions)

    def add_variables(self, variables):
        self.variables.update(variables)

    def add_operators(self, operators):
        self.operators.update(operators)

    def run_action(self, action):
        func = self.actions.get(action['func'])
        if not func:
            raise InvalidAction(f"Invalid action `{action['func']}'")

        params = action['params']
        # this exception does not happen with actual compiled script
        if params is None:
            raise InvalidActionParams(f"Params not provided for action `{action['func']}'")

        func(*params)

    def evaluate_expr(self, expr):
        logger.debug(f'{expr} = ?')

        if isinstance(expr, dict):

            operator = self.operators.get(expr['operator'])
            if not operator:
                raise InvalidOperator(f"Invalid operator `{expr['operator']}'")

            result = operator(*[self.evaluate_expr(operand) for operand in expr['operands']])

        elif isinstance(expr, str) and expr.startswith('$'):
            variable = self.variables.get(expr)
            if not variable:
                raise InvalidVariable(f"Invalid variable `{expr}'")

            result = variable()

        else:
            result = expr

        logger.debug(f'{expr} => {result}')
        return result

    def run_block(self, block):
        if isinstance(block, list):
            for s in block:
                self.run_statement(s)
        else:
            self.run_statement(block)

    def run_statement(self, statement):
        # if statement
        if 'if' in statement:
            if self.evaluate_expr(statement['if']):
                self.run_block(statement['then'])
            elif 'else' in statement:
                self.run_block(statement['else'])

        # action statement
        elif 'func' in statement:
            self.run_action(statement)

    def run_script(self, script):
        for statement in script['statements']:
            self.run_statement(statement)
