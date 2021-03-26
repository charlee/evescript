================
Overview
================

**EveScript** is a simple script language for event-based automation tasks.

::

  from evescript.compiler import EveScriptCompiler
  from evescript.executor import EveScriptExecutor

  script = '''
  if ($lightSensor > 20) {
    say("It's daytime now!")
  }
  '''

  def lightSensor():
      return read_light_sensor_port()

  compiler = EveScriptCompiler()
  compiled_script = compiler.compile(script)

  executor = EveScriptExecutor({
      'actions': { 'say': lambda x: print(x) },
      'variables': { '$lightSensor': lightSensor },
  })

  executor.run_script(compiled_script)
  # Out: It's daytime now!


EveScript allows you to write simple event-based scripts that evaluate various conditions
and execute actions. The conditions and actions are highly customizable to maximize the 
flexibility. EveScript can be used in embedded systems (such as Raspberry Pi) to implement
a flexible event-based system.


Installation
------------

::

  pip install evescript
