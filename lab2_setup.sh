#!/bin/bash
swig -python calki.i
python setup.py build_ext --inplace
