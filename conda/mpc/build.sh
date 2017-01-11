./configure --prefix=$PREFIX \
    --with-gmp=$PREFIX \
    --with-mpfr=$PREFIX \
    --enable-shared=no \
    --target=x86_64-unknown-linux-gnu

make
make check
make install
