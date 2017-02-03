./configure --prefix=$PREFIX \
    --with-gmp=$PREFIX
    	
make
make check
make install