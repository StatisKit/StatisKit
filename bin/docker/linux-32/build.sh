set -ve

git clone --recursive http://github.com/StatisKit/StatisKit

cd StatisKit/bin/conda
conda build python-scons \
            scons-tools \
            libtoolchain \
            python-toolchain \
            boost-suite \
            boost-meta \
            python-parse \
            --old-build-string

cd ../../share/git/ClangLite/bin/conda
conda build llvm \
            clang \
            libclanglite \
            python-clanglite \
            --old-build-string

cd ../../../AutoWIG/bin/conda
conda build python-autowig \
            --old-build-string

set +ve