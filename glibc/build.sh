git checkout --track -b local_glibc-2.23 origin/release/2.23/master

mkdir build
cd build

export CC=cc
export CXX=c++
export PKG_CONFIG_PATH=$PREFIX/lib/pkgconfig
export CFLAGS="-m64 -pipe -O2"
export CXXFLAGS="${CFLAGS}"
export CPPFLAGS="-I$PREFIX/include"
export LDFLAGS="-L$PREFIX/lib"
../configure --prefix=$PREFIX
make
make install