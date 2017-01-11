#!/bin/bash

chmod +x configure

if [ `uname` == Darwin ]; then
    ./configure --prefix=$PREFIX --enable-cxx
else
    ./configure --prefix=$PREFIX --host=x86_64-unknown-linux-gnu
fi

make
# make check
make install
