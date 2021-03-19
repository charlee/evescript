---
title: Overview
---

+---------+-----------------------------------------------------------+
| docs    | [![Docum                                                  |
|         | entation Status](https://readthedocs.org/projects/evescri |
|         | pt/badge/?style=flat)](https://evescript.readthedocs.io/) |
+---------+-----------------------------------------------------------+
| tests   | | [![Travis-CI Build Statu                                |
|         | s](https://api.travis-ci.com/charlee/evescript.svg?branch |
|         | =master)](https://travis-ci.com/github/charlee/evescript) |
|         | |                                                         |
+---------+-----------------------------------------------------------+
| package | |                                                         |
|         |  [![PyPI Package latest release](https://img.shields.io/p |
|         | ypi/v/evescript.svg)](https://pypi.org/project/evescript) |
|         |   [![PyPI Wheel](https://img.shields.io/pypi/             |
|         | wheel/evescript.svg)](https://pypi.org/project/evescript) |
|         |                                                           |
|         |  [![Supported versions](https://img.shields.io/pypi/pyver |
|         | sions/evescript.svg)](https://pypi.org/project/evescript) |
|         |   [![Support                                              |
|         | ed implementations](https://img.shields.io/pypi/implement |
|         | ation/evescript.svg)](https://pypi.org/project/evescript) |
|         | | [![Commits since latest release](https://img.shields.io |
|         | /github/commits-since/charlee/evescript/v0.0.0.svg)](http |
|         | s://github.com/charlee/evescript/compare/v0.0.0...master) |
+---------+-----------------------------------------------------------+

A simple script language for event-based automation tasks.

-   Free software: MIT license

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
