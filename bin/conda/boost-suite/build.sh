## Copyright [2017-2018] UMR MISTEA INRA, UMR LEPSE INRA,                ##
##                       UMR AGAP CIRAD, EPI Virtual Plants Inria        ##
## Copyright [2015-2016] UMR AGAP CIRAD, EPI Virtual Plants Inria        ##
##                                                                       ##
## This file is part of the StatisKit project. More information can be   ##
## found at                                                              ##
##                                                                       ##
##     http://statiskit.rtfd.io                                          ##
##                                                                       ##
## The Apache Software Foundation (ASF) licenses this file to you under  ##
## the Apache License, Version 2.0 (the "License"); you may not use this ##
## file except in compliance with the License. You should have received  ##
## a copy of the Apache License, Version 2.0 along with this file; see   ##
## the file LICENSE. If not, you may obtain a copy of the License at     ##
##                                                                       ##
##     http://www.apache.org/licenses/LICENSE-2.0                        ##
##                                                                       ##
## Unless required by applicable law or agreed to in writing, software   ##
## distributed under the License is distributed on an "AS IS" BASIS,     ##
## WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or       ##
## mplied. See the License for the specific language governing           ##
## permissions and limitations under the License.                        ##

set -ve

# unset CXXFLAGS
# unset CPPFLAGS
# unset CFLAGS
# unset LDFLAGS
# unset LDFLAGS_CC
# unset DEBUG_CFLAGS
# unset DEBUG_CXXFLAGS

INCLUDE_PATH="${PREFIX}/include"
LIBRARY_PATH="${PREFIX}/lib"

CXXFLAGS="${CXXFLAGS} -Wno-deprecated-declarations"

if [ "$(uname)" == "Darwin" ]; then
    TOOLSET=clang
fi

if [ "$(uname)" == "Linux" ]; then
    TOOLSET=gcc
fi

# http://www.boost.org/build/doc/html/bbv2/tasks/crosscompile.html
cat <<EOF > ${SRC_DIR}/tools/build/src/site-config.jam
using ${TOOLSET} : custom : ${CXX} ;
EOF

LINKFLAGS="${LINKFLAGS} -L${LIBRARY_PATH}"

./bootstrap.sh \
    --prefix="${PREFIX}" \
    --with-python="${PYTHON}" \
    --with-python-root="${PREFIX} : ${PREFIX}/include/python${PY_VER}m ${PREFIX}/include/python${PY_VER}" \
    --with-icu="${PREFIX}" \
    | tee bootstrap.log 2>&1

./b2 -q -d+2 \
    variant=release \
    address-model="${ARCH}" \
    architecture=x86 \
    debug-symbols=off \
    threading=multi \
    runtime-link=shared \
    link=static,shared \
    toolset=${TOOLSET}-custom \
    python="${PY_VER}" \
    include="${INCLUDE_PATH}" \
    cxxflags="${CXXFLAGS}" \
    linkflags="${LINKFLAGS}" \
    --without-mpi \
    --layout=system \
    -j$CPU_COUNT \
    install | tee b2.log 2>&1

# if [ "$(uname)" == "Darwin" ]; then

#     MACOSX_VERSION_MIN=10.13
#     CXXFLAGS="-mmacosx-version-min=${MACOSX_VERSION_MIN}"
#     CXXFLAGS="${CXXFLAGS} -stdlib=libc++ -std=c++11"
#     LINKFLAGS="-mmacosx-version-min=${MACOSX_VERSION_MIN}"
#     LINKFLAGS="${LINKFLAGS} -stdlib=libc++ -std=c++11 -L${LIBRARY_PATH}"

#     ./bootstrap.sh \
#         --prefix="${PREFIX}" \
#         --with-python="${PYTHON}" \
#         --with-python-root="${PREFIX} : ${PREFIX}/include/python${PY_VER}m ${PREFIX}/include/python${PY_VER}" \
#         --with-icu="${PREFIX}" \
#         | tee bootstrap.log 2>&1

#     ./b2 -q \
#         variant=release \
#         address-model=64 \
#         architecture=x86 \
#         debug-symbols=off \
#         threading=multi \
#         link=shared \
#         toolset=clang \
#         include="${INCLUDE_PATH}" \
#         cxxflags="${CXXFLAGS}" \
#         linkflags="${LINKFLAGS}" \
#         --without-mpi \
#         --layout=system \
#         -j$CPU_COUNT \
#         -d0 \
#         install | tee b2.log 2>&1
# fi

# if [ "$(uname)" == "Linux" ]; then
#     CXXFLAGS="${CXXFLAGS} -std=c++11"
#     LINKFLAGS="${LINKFLAGS} -std=c++11 -L${LIBRARY_PATH}"
    
#     ./bootstrap.sh \
#         --prefix="${PREFIX}" \
#         --with-python="${PYTHON}" \
#         --with-python-root="${PREFIX} : ${PREFIX}/include/python${PY_VER}m ${PREFIX}/include/python${PY_VER}" \
#         --with-icu="${PREFIX}" \
#         | tee bootstrap.log 2>&1

#     ./b2 -q \
#         variant=release \
#         address-model="${ARCH}" \
#         architecture=x86 \
#         debug-symbols=off \
#         threading=multi \
#         runtime-link=shared \
#         link=shared \
#         toolset=gcc \
#         python="${PY_VER}" \
#         include="${INCLUDE_PATH}" \
#         cxxflags="${CXXFLAGS}"\
#         linkflags="${LINKFLAGS}" \
#         --without-mpi \
#         --layout=system \
#         -j$CPU_COUNT \
#         -d0 \
#         install | tee b2.log 2>&1
# fi

mkdir ${SRC_DIR}/Library
mv -v ${PREFIX}/include ${SRC_DIR}/Library
mv -v ${PREFIX}/lib ${SRC_DIR}/Library

set +ve
