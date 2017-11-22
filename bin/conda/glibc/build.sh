mkdir build
cd build
../configure --prefix=$PREFIX
make > log.txt 2>&1
make install
