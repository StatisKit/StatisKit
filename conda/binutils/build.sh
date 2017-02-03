mkdir build-binutils
cd build-binutils

../configure --prefix=$PREFIX --disable-multilib #--target=x86_64-unknown-linux-gnu

make -j$CPU_COUNT
#mkdir install-binutils
make install 
#DESTDIR=$PWD/install-binutils
#rm -rf install-binutils/usr/{info,lib,man,share}
#cp -a install-binutils/* $PREFIX/
