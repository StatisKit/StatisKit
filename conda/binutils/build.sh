mkdir build
cd build

../configure --prefix="$PREFIX" #--target=x86_64-unknown-linux-gnu
make -j"$CPU_COUNT"
make install