#!/bin/bash

set -xe

if [[ "$PY3K" = "1" ]]; then
  sed -i'' -e '49,54d' setup.py
  sed -i'' -e '58,64d' script/scons
  sed -i'' -e '39d' engine/SCons/Util.py
  sed -i'' -e 's#exceptions#builtins#g' engine/SCons/Errors.py
  2to3 --output-dir=engine/SCons3 -W -n engine/SCons
  rm -rf engine/SCons
  mv engine/SCons3 engine/SCons
  2to3 -w -n script/scons
  2to3 -w -n script/sconsign
  2to3 -w -n script/scons-time
fi

$PYTHON setup.py install --standard-lib
