=====
Usage
=====

EveScript consists of a compiler ``EveScriptCompiler`` and an executor ``EveScriptExecutor``.

Write a Script
---------------

An EveScript is written in the following form:

::

  if (expression) {
    action1(...)
    action2(...)
  }

where, the expression is a bool expression, and the **actions** are a list of "function" calls.
The condition expression consists of **variables**, **operators** and constants (strings, numbers, and booleans).

**Actions**, **variables**, and **operators** are three types of entities that must be provided before the script can execute.

Here is a quick example (``quickstart.es``) for you to start script with EveScript.

::

  if ($lightSensor < 20) {
    say("It's getting dark now!")
  }

In this script, we used three entities that need to be provided when executing.

- ``$lightSensor``: This is a variable. A variable is a custom function that is provided as a data source to the script.
- ``say``: This is an action. An action is a custom function that will be called when the expression is true.

We will provide these entities in the `Run a script`_ section.

For more details, see :ref:`evescript-reference`.


Compile a Script
-----------------

An EveScript file (``*.es``) needs to be compiled before executed.
This is done by calling the ``compile()`` method in the ``EveScriptCompiler`` class.

::

  from evescript.compiler import EveScriptCompiler

  with open('quickstart.es') as f:
    script = f.read()

  compiler = EveScriptCompiler()
  compiled_script = compiler.compile(f)


Run a Script
------------

The compiled script can be executed with ``EveScriptExecutor``. When instancing ``EveScriptExecutor``,
the entities (actions, operators, and variables) used in the scripts must be provided. Each entity is a function or lambda.

::

  from evescript.executor import EveScriptExecutor

  ACTIONS = {
    'say': lambda s: print(s),
  }

  VARIABLES = {
    '$lightSensor': lambda x: 10,
  }

  # Provide the actions and the variables used in the script
  executor = EveScriptExecutor({
    'actions': ACTIONS,
    'variables': VARIABLES,
  })

  # run the first trigger
  executor.run_script(compiled_script)

Since we mocked the varialbe ``$lightSensor`` to make it always returns 10, the action will be executed and will print ``It's getting dark now!``.

Decompile a Script
------------------

Sometimes it is necessary to retrieve the script source for given compiled script. This can be done with ``EveScriptDecompiler``.
It provides a ``decompile`` method that takes a compiled script and returns the original script text.

*NOTE*: The decompiled script may not be identical to the original script - the whitespaces, new lines may differ,
and the decompiled script will not contain any comments that may have appeared in the original script.

The following snippet shows how to decompile:

::

  import os
  import sys

  from evescript.compiler import EveScriptCompiler
  from evescript.decompiler import EveScriptDecompiler

  script = '''
  if ($lightSensor < 20) {
    say("It's getting dark now!")
  }
  '''

  compiler = EveScriptCompiler()
  compiled_script = compiler.compile(script)

  decompiler = EveScriptDecompiler()
  decompiled_script = decompiler.decompile(compiled_script)

  print(decompiled_script)

