import os
import sys

from defs.actions import ACTIONS
from defs.operators import OPERATORS
from defs.variables import VARIABLES

cwd = os.path.dirname(__file__)

try:
    from evescript.compiler import EveScriptCompiler
    from evescript.executor import EveScriptExecutor
except ModuleNotFoundError:
    sys.path.append(os.path.normpath(os.path.join(cwd, '..', 'src')))
    from evescript.compiler import EveScriptCompiler
    from evescript.executor import EveScriptExecutor


with open('script.es') as f:
    script = f.read()

compiler = EveScriptCompiler()
compiled_script = compiler.compile(script)

executor = EveScriptExecutor({
    'actions': ACTIONS,
    'operators': OPERATORS,
    'variables': VARIABLES,
})

executor.run_script(compiled_script)
