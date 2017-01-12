#!/bin/bash

chmod +x configure

if [ `uname` == Darwin ]; then
    ./configure --prefix=$PREFIX --enable-cxx
else
    ./configure --prefix=$PREFIX --disable-shared --enable-static
fi

make
# make check
make install
