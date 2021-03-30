import unittest

import antlr4

from evescript.compiler import EveScriptCompiler

simple_script = '''
    if ($var > 0) {
        action("$var > 0")
    }
'''

simple_script_ast = {
    'statements': [{
        'if': {'operator': '>', 'operands': ['$var', 0]},
        'then': {'func': 'action', 'params': ['$var > 0']},
    }]
}

constant_expr = '''
    if (true) {
    }
'''

constant_expr_ast = {
    'statements': [{
        'if': True,
        'then': [],
    }]
}

complex_expr = '''
    if ($var1 > 1 && $var2 < 2 || $var3 >= 3 && $var4 <= 4 && ($var5 != 5.0 || !($var6 == 0.6))) {
        action("success")
    }
'''

complex_expr_ast = {
    'operator': '||',
    'operands': [
        {
            'operator': '&&',
            'operands': [
                {'operator': '>', 'operands': ['$var1', 1]},
                {'operator': '<', 'operands': ['$var2', 2]},
            ]
        },
        {
            'operator': '&&',
            'operands': [
                {'operator': '>=', 'operands': ['$var3', 3]},
                {
                    'operator': '&&',
                    'operands': [
                        {'operator': '<=', 'operands': ['$var4', 4]},
                        {
                            'operator': '||',
                            'operands': [
                                {'operator': '!=', 'operands': ['$var5', 5.0]},
                                {
                                    'operator': '!',
                                    'operands': [{
                                        'operator': '==',
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
    if ($var1 match "abc") {
        action("success")
    }
    if ($var2 < 0) {
        action("fail")
    }
'''

multi_conditions_ast = {
    'statements': [
        {'if': {'operator': 'match', 'operands': ['$var1', "abc"]}, 'then': {'func': 'action', 'params': ['success']}},
        {'if': {'operator': '<', 'operands': ['$var2', 0]}, 'then': {'func': 'action', 'params': ['fail']}},
    ]
}

multi_actions = '''
    if ($var1 > 0) {
        action1("success", true)
        action2("fail", false, 2)
    }
'''

multi_actions_ast = {
    'statements': [
        {
            'if': {'operator': '>', 'operands': ['$var1', 0]},
            'then': [
                {'func': 'action1', 'params': ['success', True]},
                {'func': 'action2', 'params': ['fail', False, 2]}
            ]
        },
    ]
}

zero_actions = '''
    if ($var1 > 0) {
    }
'''

zero_actions_ast = {
    'statements': [
        {'if': {'operator': '>', 'operands': ['$var1', 0]}, 'then': []},
    ]
}

empty_param_action = '''
    if (true) {
        test()
    }
'''

empty_param_action_ast = {
    'statements': [
        {
            'if': True,
            'then': {'func': 'test', 'params': []},
        },
    ]
}

standalone_action = '''
test()
'''

standalone_action_ast = {
    'statements': [
        {'func': 'test', 'params': []}
    ]
}

nested_if = '''
if (true) {
    if (false) {
        test()
    }
}
'''

nested_if_ast = {
    'statements': [
        {
            'if': True,
            'then': {
                'if': False,
                'then': {'func': 'test', 'params': []}
            }
        }
    ]
}

if_else = '''
if (true) {
    action1()
    action1()
} else if (false) {
    action2()
} else
    action3()
'''

if_else_ast = {
    'statements': [
        {
            'if': True,
            'then': [
                {'func': 'action1', 'params': []},
                {'func': 'action1', 'params': []},
            ],
            'else': {
                'if': False,
                'then': {'func': 'action2', 'params': []},
                'else': {'func': 'action3', 'params': []},
            }
        }
    ]
}

syntax_error = '''
-
'''

comment = '''
# empty
'''

comment_ast = {
    'statements': []
}


class CompilerTestCase(unittest.TestCase):

    def setUp(self):
        self.compiler = EveScriptCompiler()

    def tearDown(self):
        pass

    def test_simple_script(self):
        ast = self.compiler.compile(simple_script)
        self.assertEqual(ast, simple_script_ast)

    def test_constant_expr(self):
        ast = self.compiler.compile(constant_expr)
        self.assertEqual(ast, constant_expr_ast)

    def test_complex_expr(self):
        ast = self.compiler.compile(complex_expr)
        self.assertEqual(ast['statements'][0]['if'], complex_expr_ast)

    def test_multi_conditions(self):
        ast = self.compiler.compile(multi_conditions)
        self.assertEqual(ast, multi_conditions_ast)

    def test_multi_actions(self):
        ast = self.compiler.compile(multi_actions)
        self.assertEqual(ast, multi_actions_ast)

    def test_zero_actions(self):
        ast = self.compiler.compile(zero_actions)
        self.assertEqual(ast, zero_actions_ast)

    def test_empty_param_action(self):
        ast = self.compiler.compile(empty_param_action)
        self.assertEqual(ast, empty_param_action_ast)

    def test_syntax_error(self):
        with self.assertRaises(antlr4.error.Errors.ParseCancellationException):
            self.compiler.compile(syntax_error, raise_exceptions=True)

    def test_comment(self):
        ast = self.compiler.compile(comment, True)
        self.assertEqual(ast, comment_ast)

    def test_standalone_action(self):
        ast = self.compiler.compile(standalone_action, True)
        self.assertEqual(ast, standalone_action_ast)

    def test_nested_if(self):
        ast = self.compiler.compile(nested_if, True)
        self.assertEqual(ast, nested_if_ast)

    def test_if_else(self):
        ast = self.compiler.compile(if_else, True)
        self.assertEqual(ast, if_else_ast)
