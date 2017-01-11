./configure --prefix=$PREFIX \
    --with-gmp=$PREFIX \
    --enable-static \
    --target=x86_64-unknown-linux-gnu

make
make check
make install