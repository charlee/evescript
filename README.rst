========
Overview
========

A simple script language for event-based automation tasks.

* Free software: MIT license

Installation
============

::

    pip install evescript

You can also install the in-development version with::

    pip install https://github.com/charlee/evescript/archive/master.zip


Documentation
=============


..
  https://evescript.readthedocs.io/


Development
===========

To run all the tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox
