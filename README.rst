========
Overview
========

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

.. |commits-since| image:: https://img.shields.io/github/commits-since/charlee/evescript/v0.0.0.svg
    :alt: Commits since latest release
    :target: https://github.com/charlee/evescript/compare/v0.0.0...master



.. end-badges

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
