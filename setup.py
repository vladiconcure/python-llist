#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, Extension

sources = [
    'src/c_extension/llist.c',
    'src/c_extension/dllist.c',
    'src/c_extension/sllist.c',
    'src/c_extension/utils.c',
]

ext_modules = [
    Extension(
        'llistplus._llist',
        sources=sources,
        include_dirs=['src/c_extension'],
    )
]

setup(
    ext_modules=ext_modules,
)
