set -ve

source activate
rm -rf ${CONDA_PREFIX}/conda-bld

cd ../../conda
conda build python-scons \
            scons-tools \
            libtoolchain \
            python-toolchain \
            boost-suite \
            boost-meta \
            python-parse

cd ../../share/git/ClangLite/bin/conda
conda build llvm \
            clang \
            libclanglite \
            python-clanglite

cd ../../../AutoWIG/bin/conda
conda build python-autowig

cd ../../../../../../bin/conda
conda build statiskit-dev

cd ../script/linux

set +ve