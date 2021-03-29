import unittest

from evescript.compiler import EveScriptCompiler
from evescript.decompiler import EveScriptDecompiler

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
    if ($var1 > 1 && $var2 < 2 || $var3 >= 3 && $var4 <= 4 && ($var5 != 5.0 || !($var6 == 0.6))) {
        action("success")
    }
'''

multi_conditions = '''
    if ($var1 match "abc") {
        action("success")
    }
    if ($var2 < 0) {
        action("fail")
    }
'''

zero_actions = '''
    if ($var1 > 0) {
    }
'''

empty_param_action = '''
    if (true) {
        test()
    }
'''

standalone_action = '''
test()
'''

nested_if = '''
if (true) {
    if (false) {
        test()
    }
}
'''


class DecompilerTestCase(unittest.TestCase):

    def setUp(self):
        self.compiler = EveScriptCompiler()
        self.decompiler = EveScriptDecompiler()

    def tearDown(self):
        pass

    def assertDecompile(self, ast):
        """Assert the decompiled script can be compiled to the same AST."""
        decomp = self.decompiler.decompile(ast)
        recomp = self.compiler.compile(decomp)
        self.assertDictEqual(ast, recomp)

    def test_simple_script(self):
        ast = self.compiler.compile(simple_script)
        self.assertDecompile(ast)

    def test_complex_expr(self):
        ast = self.compiler.compile(complex_expr)
        self.assertDecompile(ast)

    def test_multi_conditions(self):
        ast = self.compiler.compile(multi_conditions)
        self.assertDecompile(ast)

    def test_multi_actions(self):
        ast = self.compiler.compile(multi_actions)
        self.assertDecompile(ast)

    def test_standalone_action(self):
        ast = self.compiler.compile(standalone_action)
        self.assertDecompile(ast)

    def test_nested_if(self):
        ast = self.compiler.compile(nested_if)
        self.assertDecompile(ast)
