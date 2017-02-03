./configure --prefix=$PREFIX \
    --with-gmp=$PREFIX \
    --with-mpfr=$PREFIX \
    
make
make check
make install
