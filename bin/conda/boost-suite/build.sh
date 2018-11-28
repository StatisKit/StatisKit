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

python ${RECIPE_DIR}/filter.py --src=${PREFIX} --dst=filtered.pkl

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

if [[ "${CI}" = "true" ]]; then
    export DFLAG="+1"
else
    export DFLAG="+2"
fi

./bootstrap.sh \
    --prefix="${PREFIX}" \
    --with-python="${PYTHON}" \
    --without-libraries=system \
    --with-python-root="${PREFIX} : ${PREFIX}/include/python${PY_VER}m ${PREFIX}/include/python${PY_VER}" \
    --with-icu="${PREFIX}" \
    | tee bootstrap.log 2>&1

./b2 -q -d${DFLAG} \
    variant=release \
    address-model="${ARCH}" \
    architecture=x86 \
    debug-symbols=off \
    threading=multi \
    runtime-link=shared \
    link=shared \
    toolset=${TOOLSET}-custom \
    python="${PY_VER}" \
    include="${INCLUDE_PATH}" \
    cxxflags="${CXXFLAGS}" \
    linkflags="${LINKFLAGS}" \
    --without-mpi \
    --layout=system \
    -j$CPU_COUNT \
    install | tee b2.log 2>&1

python ${RECIPE_DIR}/move.py --src=${PREFIX}/include --dst=${SRC_DIR}/Library/include --filtered=filtered.pkl
python ${RECIPE_DIR}/move.py --src=${PREFIX}/lib --dst=${SRC_DIR}/Library/lib --filtered=filtered.pkl

set +ve
