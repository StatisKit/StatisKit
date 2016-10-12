#!/bin/bash

set -xe

python bootstrap.py build/scons
cd build/scons
python setup.py install --standard-lib

# $PYTHON setup.py install --standard-lib
