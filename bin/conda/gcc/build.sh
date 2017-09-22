ln -s $PREFIX/lib $PREFIX/lib64

echo 'gcc version' 
gcc -v

#export TMPDIR=/media/osboxes/New/tmpdir
export TMPDIR=$PWD/tmpdir

#./contrib/download_prerequisites

cd ..		
mkdir objdir		
cd objdir


if [ "$(uname)" == "Darwin" ]; then
    export LDFLAGS="-Wl,-headerpad_max_install_names"
    export BOOT_LDFLAGS="-Wl,-headerpad_max_install_names"

     $PWD/../gcc-7.1.1-20170718/configure \
        --prefix=$PREFIX \
        --disable-multilib \
        --enable-languages=c,c++ 
        --libdir=$PREFIX/lib \
        --with-gmp=$PREFIX \
        --with-mpfr=$PREFIX \
        --with-mpc=$PREFIX \
        --with-isl=$PREFIX \
        --with-cloog=$PREFIX \
        --with-boot-ldflags=$LDFLAGS \
        --with-stage1-ldflags=$LDFLAGS \

else
    # For reference during post-link.sh, record some
    # details about the OS this binary was produced with.
    #mkdir -p ${PREFIX}/share
    #cat /etc/*-release > ${PREFIX}/share/conda-gcc-build-machine-os-details
    
      $PWD/../gcc-7.1.1-20170718/configure \
        --build=x86_64-linux-gnu \
        --host=x86_64-linux-gnu \
        --target=x86_64-linux-gnu \
        --prefix=$PREFIX \
        --libdir=$PREFIX/lib \
        --with-gmp=$PREFIX \
        --with-mpfr=$PREFIX \
        --with-mpc=$PREFIX \
        --with-isl=$PREFIX \
        --with-cloog=$PREFIX \
        --enable-checking=release \
        --disable-multilib \
        --enable-languages=c,c++
fi
make
make install
rm $PREFIX/lib64

# Link cc to gcc
(cd $PREFIX/bin && ln -s gcc cc)

