llist - linked lists for CPython (fork)
================================

llist is an extension module for CPython providing basic linked list
data structures.
Collections implemented in the llist module perform well in problems
which rely on fast insertions and/or deletions of elements in
the middle of a sequence.
For this kind of workload, they can be significantly faster than
collections.deque or standard Python lists.

## Fork installation

install with preserving the original package name:
```bash
pip install git+https://github.com/vladiconcure/python-llist
```
install with a new package name(llistplus) to avoid conflicts with the original package:
```bash
pip install git+https://github.com/vladiconcure/python-llist@rename/llistplus
```

## Fork Features

This is an enhanced fork of the original:
- [python-llist](https://github.com/ajakubek/python-llist)      
- [pypy-llist/](http://github.com/rgsoda/pypy-llist/)     
with the following improvements:

- **🔄 Automatic Fallback**: Seamlessly falls back to pure Python implementation when C extension fails to build/import
- **📦 Modern Build System**: Uses `pyproject.toml` with proper dependencies and build configuration  
- **🏗️ Unified Structure**: Clean project organization with both C and Python implementations in one package
- **✅ Full Compatibility**: Zero breaking changes - all existing code works unchanged
- **🔧 Enhanced API**: Pure Python version now includes all iterator classes (`dllistiterator`, `sllistnodeiterator`, etc.)

Use `llist.using_c_extension()` to check which implementation is active.

This extension requires Python 3.7 or newer. The package automatically provides both fast C extension and pure Python fallback implementations with identical APIs.

Currently llist provides the following types of linked lists:
 - dllist - a doubly linked list
 - sllist - a singly linked list

Full documentation of these classes is available at:
https://ajakubek.github.io/python-llist/index.html

To install this package, run "pip install llist".
Alternatively you can also download it manually from http://pypi.python.org/pypi, unpack into a directory and build/install with the following commands:
```
python -m build
pip install .
```
The instruction assumes that the 'build' frontend is already available in site-packages.

The most current development version is available at:
https://github.com/ajakubek/python-llist/

Bugs can be reported at:
https://github.com/ajakubek/python-llist/issues

This software is distributed under the MIT license.
Please see the LICENSE file included in the package for details.

[![Build Status](https://github.com/ajakubek/python-llist/actions/workflows/python-package.yml/badge.svg?branch=master)](https://github.com/ajakubek/python-llist/actions/workflows/python-package.yml?query=branch%3Amaster)
