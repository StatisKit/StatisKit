set -ve

INCLUDE_PATH="${PREFIX}/include"
LIBRARY_PATH="${PREFIX}/lib"

CXXFLAGS="${CXXFLAGS} -fPIC"

if [ "$(uname)" == "Darwin" ]; then
    MACOSX_VERSION_MIN=10.7
    CXXFLAGS="-mmacosx-version-min=${MACOSX_VERSION_MIN}"
    CXXFLAGS="${CXXFLAGS} -stdlib=libc++ -std=c++11"
    LINKFLAGS="-mmacosx-version-min=${MACOSX_VERSION_MIN}"
    LINKFLAGS="${LINKFLAGS} -stdlib=libc++ -std=c++11 -L${LIBRARY_PATH}"

    ./bootstrap.sh \
        --prefix="${PREFIX}" \
        --with-python="${PYTHON}" \
        --with-python-root="${PREFIX} : ${PREFIX}/include/python${PY_VER}m ${PREFIX}/include/python${PY_VER}" \
        --with-icu="${PREFIX}" \
        | tee bootstrap.log 2>&1

    ./b2 -q \
        variant=release \
        address-model=64 \
        architecture=x86 \
        debug-symbols=off \
        threading=multi \
        link=shared \
        toolset=clang \
        include="${INCLUDE_PATH}" \
        cxxflags="${CXXFLAGS}" \
        linkflags="${LINKFLAGS}" \
        -j$CPU_COUNT \
        -d0 \
        install | tee b2.log 2>&1
fi

if [ "$(uname)" == "Linux" ]; then
    CXXFLAGS="${CXXFLAGS} -std=c++11 -D_GLIBCXX_USE_CXX11_ABI=1"
    LINKFLAGS="${LINKFLAGS} -std=c++11 -L${LIBRARY_PATH}"
    
    ./bootstrap.sh \
        --prefix="${PREFIX}" \
        --with-python="${PYTHON}" \
        --with-python-root="${PREFIX} : ${PREFIX}/include/python${PY_VER}m ${PREFIX}/include/python${PY_VER}" \
        | tee bootstrap.log 2>&1

    ./b2 -q \
        variant=release \
        address-model="${ARCH}" \
        architecture=x86 \
        debug-symbols=off \
        threading=multi \
        runtime-link=shared \
        link=shared \
        toolset=gcc \
        python="${PY_VER}" \
        include="${INCLUDE_PATH}" \
        cxxflags="${CXXFLAGS}"\
        linkflags="${LINKFLAGS}" \
        --layout=system \
        -j$CPU_COUNT \
        -d0 \
        install | tee b2.log 2>&1
fi

set +ve