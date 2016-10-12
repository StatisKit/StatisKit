#!/bin/bash

set -xe

if [[ "$PY3K" = "1" ]]; then
  sed -i'' -e'49,54d' setup.py
  2to3 --output-dir=engine/SCons3 -W -n engine/SCons
  rm -rf engine/SCons
  mv engine/SCons3 engine/SCons
  2to3 --output-dir=script3 -W -n script
  rm -rf script
  mv script3 script
fi

$PYTHON setup.py install --standard-lib
