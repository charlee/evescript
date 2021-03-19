EveScript
=============

[![Documentation Status](https://readthedocs.org/projects/evescript/badge/?style=flat)](https://evescript.readthedocs.io/)
[![Travis-CI Build Status](https://api.travis-ci.com/charlee/evescript.svg?branch=master)](https://travis-ci.com/github/charlee/evescript)

A simple script language for event-based automation tasks.

# Installation

    pip install evescript

You can also install the in-development version with:

    pip install https://github.com/charlee/evescript/archive/master.zip

# Documentation

<https://evescript.readthedocs.io/>

# Development

To run all the tests run:

    tox

Note, to combine the coverage data from all the tox environments run:

+------+---------------------------------------------------------------+
| Win  |     set PYTEST_ADDOPTS=--cov-append                           |
| dows |     tox                                                       |
+------+---------------------------------------------------------------+
| O    |     PYTEST_ADDOPTS=--cov-append tox                           |
| ther |                                                               |
+------+---------------------------------------------------------------+
