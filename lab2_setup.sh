#!/bin/bash
swig -python calki.i
python3 setup.py build_ext --inplace
