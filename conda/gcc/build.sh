#!/bin/bash

# Install gcc to its very own prefix.
# GCC must not be installed to the same prefix as the environment,
# because $GCC_PREFIX/include is automatically considered to be a
# "system" header path.
# That could cause -I$PREFIX/include to be essentially ignored in users' recipes
# (It would still be on the search path, but it would be in the wrong position in the search order.)
# .. Unfortunately:
#    1. Worked by relying on failure to relocate paths (until this commit).
#    2. .. and then not finding unrelocated folders, worse, if build from /root/miniconda3 as linux-32 4.8.5-3 was
#    3. .. led to 'Permission denied' failures from attempting to still access those unrelocated paths.
#    The current implementation fixes it by making libiberty's relocation code capable of handling '..' and then
#    configuring the various other (non-prefix) dirs as relative to '${GCC_PREFIX}/..'. This turns the two
#    'Permission Denied' errors into 'ignoring duplicate directory'.
# I disagree with the motivation behind this change. What it does is prevents #include <GL/gl.h> from finding
#  Conda's version of gl.h, should we wish to use a custom one (angleproject for example) unless the user
#  specifies -I${PREFIX}/include, and when they do that, that path is added to the *front* of the system
#  includes path, which is *not* where it is meant to be. It is meant to appear between /usr/local/include and
#  /usr/include as a block of 3 final system includes, and all of that comes after GCCs own headers and those
#  from libstdc++. I will revist this later.

# ./contrib/download_prerequisites

# #ln -sf binutils-2.27 binutils || exit 1
# wget https://ftp.gnu.org/gnu/binutils/binutils-2.26.1.tar.bz2 || exit 1
# tar xjf binutils-2.26.1.tar.bz2 || exit 1
# set +e
# for file in ./binutils-2.26.1/*; do
#     echo $file
#     if [[ ! ( -f "../$file" || -d "../$file" ) ]]; then
#         ln -s "$file"
#     fi
# done
# set -e
# cd ..
# mkdir build && cd build
#exit 1
# rsync -av binutils-2.27/bfd bfd || exit 1
# rsync -av binutils-2.27/binutils binutils || exit 1
# rsync -av binutils-2.27/config c++config || exit 1
# rsync -av binutils-2.27/elfcpp elfcpp || exit 1
# rsync -av binutils-2.27/etc etc || exit 1
# rsync -av binutils-2.27/gas gas || exit 1
# rsync -av binutils-2.27/gold gold || exit 1
# rsync -av binutils-2.27/gprof gprof || exit 1
# rsync -av binutils-2.27/include include || exit 1
# rsync -av binutils-2.27/intl intl || exit 1
# rsync -av binutils-2.27/ld ld || exit 1
# rsync -av binutils-2.27/libiberty libiberty || exit 1
# rsync -av binutils-2.27/opcodes opcodes || exit 1
# rsync -av binutils-2.27/zlib zlib || exit 1

# wget http://ftp.gnu.org/pub/gnu/libiconv/libiconv-1.13.tar.gz  || exit 1
# tar -xvzf libiconv-1.13.tar.gz || exit 1
# ln -sf libiconv-1.13 libiconv || exit 1

# wget https://ftp.gnu.org/gnu/bison/bison-2.5.tar.bz2
# tar xjf bison-2.5.tar.bz2 || exit 1
# ln -sf bison-2.5 bison || exit 1

# wget https://github.com/westes/flex/releases/download/v2.6.3/flex-2.6.3.tar.gz
# tar -xvzf flex-2.6.3.tar.gz || exit 1
# ln -sf flex-2.6.3 flex || exit 1

# ls
# ls flex
# ls bison

# # exit 1

unset LIBRARY_PATH CPATH C_INCLUDE_PATH PKG_CONFIG_PATH CPLUS_INCLUDE_PATH INCLUDE LD_LIBRARY_PATH

GCC_PREFIX="$PREFIX/gcc"
mkdir "$GCC_PREFIX"

ln -s "$PREFIX/lib" "$PREFIX/lib64"

if [ "$(uname)" == "Darwin" ]; then
    # On Mac, we expect that the user has installed the xcode command-line utilities (via the 'xcode-select' command).
    # The system's libstdc++.6.dylib will be located in /usr/lib, and we need to help the gcc build find it.
    export LDFLAGS="-Wl,-headerpad_max_install_names,-rpath,${PREFIX}/lib -Wl,-L${PREFIX}/lib -Wl,-L/usr/lib"
    export DYLD_FALLBACK_LIBRARY_PATH="$PREFIX/lib:/usr/lib"

    ./configure \
        --prefix="$GCC_PREFIX" \
        --with-gxx-include-dir="$GCC_PREFIX/include/c++" \
        --bindir="$GCC_PREFIX/../bin" \
        --datarootdir="$GCC_PREFIX/../share" \
        --libdir="$GCC_PREFIX/../lib" \
        --with-gmp="$PREFIX" \
        --with-mpfr="$PREFIX" \
        --with-mpc="$PREFIX" \
        --with-isl="$PREFIX" \
        --with-boot-ldflags="$LDFLAGS" \
        --with-stage1-ldflags="$LDFLAGS" \
        --enable-checking=release \
        --with-tune=generic \
        --disable-multilib
else
    # For reference during post-link.sh, record some
    # details about the OS this binary was produced with.
    mkdir -p "${PREFIX}/share"
    cat /etc/*-release > "$PREFIX/share/conda-gcc-build-machine-os-details"

    # ./configure \
    #     --prefix="$GCC_PREFIX" \
    #     --enable-clocale=gnu \
    #     --enable-shared --enable-threads=posix --enable-__cxa_atexit \
    #     --disable-nls --disable-multilib \
    #     --with-gxx-include-dir="$GCC_PREFIX/include/c++" \
    #     --bindir="$GCC_PREFIX/../bin" \
    #     --datarootdir="$GCC_PREFIX/../share" \
    #     --libdir="$GCC_PREFIX/../lib" \
    #     --enable-checking=release \
    #     --with-tune=generic \
    ./configure \
        --disable-bootstrap \
        --disable-libstdcxx-pch \
        --enable-libgomp \
        --enable-lto \
        --enable-threads=posix \
        --enable-tls \
        --with-fpmath=sse \
        --prefix="$GCC_PREFIX" \
        --with-gxx-include-dir="$GCC_PREFIX/include/c++" \
        --bindir="$GCC_PREFIX/../bin" \
        --datarootdir="$GCC_PREFIX/../share" \
        --libdir="$GCC_PREFIX/../lib" \
        --with-gmp="$PREFIX" \
        --with-mpfr="$PREFIX" \
        --with-mpc="$PREFIX" \
        --with-isl="$PREFIX" \
        --with-cloog="$PREFIX" \
        --enable-checking=release \
        --with-tune=generic \
        --disable-multilib \
        --enable-languages=c,c++ \
        #--target=x86_64-unknown-linux-gnu
fi

# # Split compilation into stages so OS X is satisfied
# make all-gcc -j$CPU_COUNT
# make all-target-libgcc -j$CPU_COUNT
# make install-gcc install-target-libgcc
# make all-target-libstdc++-v3 -j$CPU_COUNT
# make install-target-libstdc++-v3
# make -j$CPU_COUNT
# make install-strip
make -j$CPU_COUNT
make install

rm "$PREFIX/lib64"

# Fix libtool paths
find "$PREFIX" -name '*.la' -print0 | xargs -0  sed -i.backup 's%lib/../lib64%lib%g'
find "$PREFIX" -name '*la.backup' -print0 | xargs -0  rm -f

# Link cc to gcc
(cd "$PREFIX"/bin && ln -s gcc cc)
