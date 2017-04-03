#!/usr/bin/env python3

from distutils.core import setup, Extension


calki_module = Extension('_calki',
                           sources=['calki_wrap.c', 'calki.c'],
                           )

setup (name = 'calki',
       version = '0.1',
       author      = "SWIG Docs",
       description = """Simple swig example from docs""",
       ext_modules = [calki_module],
       py_modules = ["calki"],
       )
