import unittest
from unittest.mock import Mock

from evescript.compiler import EveScriptCompiler
from evescript.exceptions import InvalidAction, InvalidOperator, InvalidVariable
from evescript.executor import EveScriptExecutor

actions = {
    'say': Mock(),
    'play': Mock(),
}

operators = {
    'match': Mock(),
}

variables = {
    '$var1': Mock(),
    '$var2': Mock(),
    '$var3': Mock(),
}

simple_script = '''
    if ($var1 > 0) {
        say("$var1 > 0")
    }
'''

multi_actions = '''
    if ($var1 > 0 && $var2 < 0) {
        say("$var1 > 0")
        play("$var2 < 0")
    }
'''

complex_expr = '''
    if (($var1 match "abc" || $var2 < 0) && ($var3 == 0)) {
        say("success")
    }
'''

ivnalid_action = '''
    if ($var1 > 0) {
        test("$var1 > 0")
    }
'''

ivnalid_variable = '''
    if ($invalid > 0) {
    }
'''

ivnalid_operator = '''
    if ($var1 invalidOperator 0) {
    }
'''


class ExecutorTestCase(unittest.TestCase):

    def setUp(self):
        for mock in [*list(actions.values()), *list(operators.values()), *list(variables.values())]:
            mock.reset_mock()

        self.compiler = EveScriptCompiler()
        self.executor = EveScriptExecutor({
            'actions': actions,
            'operators': operators,
            'variables': variables,
        })

    def tearDown(self):
        pass

    def test_simple_script(self):
        variables['$var1'].return_value = 1

        ast = self.compiler.compile(simple_script)
        self.executor.run_script(ast)

        variables['$var1'].assert_called()
        actions['say'].assert_called_with('$var1 > 0')

    def test_multi_actions(self):
        variables['$var1'].return_value = 1
        variables['$var2'].return_value = -1

        ast = self.compiler.compile(multi_actions)
        self.executor.run_script(ast)

        variables['$var1'].assert_called()
        variables['$var2'].assert_called()
        actions['say'].assert_called_with('$var1 > 0')
        actions['play'].assert_called_with('$var2 < 0')

    def test_complex_expr(self):
        variables['$var2'].return_value = -1
        variables['$var3'].return_value = 0
        operators['match'].return_value = True

        ast = self.compiler.compile(complex_expr)
        self.executor.run_script(ast)

        variables['$var1'].assert_called()
        variables['$var2'].assert_called()
        variables['$var3'].assert_called()
        operators['match'].assert_called()
        actions['say'].assert_called_with('success')

    def test_complex_expr_fail(self):
        variables['$var2'].return_value = 1
        variables['$var3'].return_value = 0
        operators['match'].return_value = False

        ast = self.compiler.compile(complex_expr)
        self.executor.run_script(ast)

        variables['$var1'].assert_called()
        variables['$var2'].assert_called()
        variables['$var3'].assert_called()
        operators['match'].assert_called()
        actions['say'].assert_not_called()

    def test_invalid_action(self):
        variables['$var1'].return_value = 1
        ast = self.compiler.compile(ivnalid_action)

        with self.assertRaises(InvalidAction):
            self.executor.run_script(ast)

    def test_invalid_variable(self):
        variables['$var1'].return_value = 1
        ast = self.compiler.compile(ivnalid_variable)

        with self.assertRaises(InvalidVariable):
            self.executor.run_script(ast)

    def test_invalid_operator(self):
        variables['$var1'].return_value = 1
        ast = self.compiler.compile(ivnalid_operator)

        with self.assertRaises(InvalidOperator):
            self.executor.run_script(ast)
