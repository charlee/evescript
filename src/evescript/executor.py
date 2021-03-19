import sys
import logging
from copy import copy

from .exceptions import InvalidOperator, InvalidVariable

logger = logging.getLogger(__name__)
handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.DEBUG)
logger.addHandler(handler)

logger.setLevel(logging.INFO)

DEFAULT_OPERATORS = {
    # Logical operators
    'and': lambda a, b: a and b,
    'or': lambda a, b: a or b,
    'not': lambda a: not a,

    # Comparison operatos
    'lt': lambda a, b: a < b,
    'lte': lambda a, b: a <= b,
    'gt': lambda a, b: a > b,
    'gte': lambda a, b: a >= b,
    'eq': lambda a, b: a == b,
    'ne': lambda a, b: a != b,
}

class EveScriptExector:


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


    def run_trigger(self, trigger):

        for condition in trigger['conditions']:
            if self.evaluate_expr(condition['if']):
                for action in condition['then']:
                    self.run_action(action)
