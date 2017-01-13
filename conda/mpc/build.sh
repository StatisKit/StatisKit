./configure --prefix=$PREFIX \
    --with-gmp=$PREFIX \
    --with-mpfr=$PREFIX \
    --disable-shared \
    
make
make check
make install
