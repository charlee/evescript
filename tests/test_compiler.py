import unittest
from evescript.compiler import EveScriptCompiler


simple_script = '''
on (timer) {
    if ($var > 0) {
        action("$var > 0")
    }
}
'''

simple_script_ast = {
    'triggers': [{
        'event': 'timer',
        'conditions': [{
            'if': { 'operator': 'gt', 'operands': ['$var', 0] },
            'then': [{ 'func': 'action', 'params': ['$var > 0'] }],
        }]
    }]
}

complex_expr = '''
    on (timer) {
        if ($var1 > 1 && $var2 < 2 || $var3 >= 3 && $var4 <= 4 && ($var5 != 5.0 || !($var6 == 0.6))) {
            action("success")
        }
    }
'''

complex_expr_ast = {
    'operator': 'or',
    'operands': [
        {
            'operator': 'and',
            'operands': [
                {'operator': 'gt', 'operands': ['$var1', 1]},
                {'operator': 'lt', 'operands': ['$var2', 2]},
            ]
        },
        {
            'operator': 'and',
            'operands': [
                { 'operator': 'gte', 'operands': ['$var3', 3] },
                {
                    'operator': 'and',
                    'operands': [
                        {'operator': 'lte', 'operands': ['$var4', 4]},
                        {
                            'operator': 'or',
                            'operands': [
                                {'operator': 'ne', 'operands': ['$var5', 5.0]},
                                {
                                    'operator': 'not',
                                    'operands': [{
                                        'operator': 'eq',
                                        'operands': ['$var6', 0.6],
                                    }]
                                },
                            ]
                        }
                    ]
                }
            ]
        }
    ]
}

multi_conditions = '''
    on (timer) {
        if ($var1 > 0) {
            action("success")
        }
        if ($var2 < 0) {
            action("fail")
        }
    }
'''

multi_conditions_ast = {
    'event': 'timer',
    'conditions': [
        { 'if': { 'operator': 'gt', 'operands': ['$var1', 0] }, 'then': [{ 'func': 'action', 'params': ['success']}]},
        { 'if': { 'operator': 'lt', 'operands': ['$var2', 0] }, 'then': [{ 'func': 'action', 'params': ['fail']}]},
    ]
}


class CompilerTestCase(unittest.TestCase):

    def setUp(self):
        self.compiler = EveScriptCompiler()

    def tearDown(self):
        pass

    def test_simple_script(self):
        ast = self.compiler.compile(simple_script)
        self.assertEqual(ast, simple_script_ast)

    def test_complex_expr(self):
        ast = self.compiler.compile(complex_expr)
        self.assertEqual(ast['triggers'][0]['conditions'][0]['if'], complex_expr_ast)

    def test_multi_conditions(self):
        ast = self.compiler.compile(multi_conditions)
        self.assertEqual(ast['triggers'][0], multi_conditions_ast)