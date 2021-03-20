import os
import sys

cwd = os.path.dirname(__file__)

try:
    from evescript.compiler import EveScriptCompiler
    from evescript.decompiler import EveScriptDecompiler
except ModuleNotFoundError:
    sys.path.append(os.path.normpath(os.path.join(cwd, '..', 'src')))
    from evescript.compiler import EveScriptCompiler
    from evescript.decompiler import EveScriptDecompiler


with open('script.es') as f:
    script = f.read()

compiler = EveScriptCompiler()
compiled_script = compiler.compile(script)

decompiler = EveScriptDecompiler()
decompiled_script = decompiler.decompile(compiled_script)

print(decompiled_script)
