================
EveScript
================

**EveScript** is a simple script language for event-based automation tasks.

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |travis|
        |
    * - package
      - | |version| |wheel| |supported-versions| |supported-implementations|
        | |commits-since|
.. |docs| image:: https://readthedocs.org/projects/evescript/badge/?style=flat
    :target: https://evescript.readthedocs.io/
    :alt: Documentation Status

.. |travis| image:: https://api.travis-ci.com/charlee/evescript.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.com/github/charlee/evescript

.. |version| image:: https://img.shields.io/pypi/v/evescript.svg
    :alt: PyPI Package latest release
    :target: https://pypi.org/project/evescript

.. |wheel| image:: https://img.shields.io/pypi/wheel/evescript.svg
    :alt: PyPI Wheel
    :target: https://pypi.org/project/evescript

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/evescript.svg
    :alt: Supported versions
    :target: https://pypi.org/project/evescript

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/evescript.svg
    :alt: Supported implementations
    :target: https://pypi.org/project/evescript

.. |commits-since| image:: https://img.shields.io/github/commits-since/charlee/evescript/0.5.0.svg
    :alt: Commits since latest release
    :target: https://github.com/charlee/evescript/compare/0.5.0...master



.. end-badges

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
