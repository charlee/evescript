import os
import json
import sys

cwd = os.path.dirname(__file__)

try:
    from evescript.executor import EveScriptExector
    from evescript.compiler import EveScriptCompiler
except ModuleNotFoundError:
    sys.path.append(os.path.normpath(os.path.join(cwd, '..', 'src')))
    from evescript.executor import EveScriptExector
    from evescript.compiler import EveScriptCompiler

from defs.operators import OPERATORS
from defs.variables import VARIABLES
from defs.actions import ACTIONS


with open('script.es') as f:
    script = f.read()

compiler = EveScriptCompiler()
compiled_script = compiler.compile(script)

executor = EveScriptExector({
    'actions': ACTIONS,
    'operators': OPERATORS,
    'variables': VARIABLES,
})

executor.run_script(compiled_script)
