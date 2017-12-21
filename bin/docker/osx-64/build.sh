set -ve

git clone --recursive http://github.com/StatisKit/StatisKit

cd StatisKit/bin/conda
conda build llvm-suite \
            python-scons \
            scons-tools \
            libtoolchain \
            python-toolchain \
            boost-suite \
            boost-meta \
            python-parse \
            --old-build-string

cd ../../share/git/ClangLite/bin/conda
git checkout v4.0.1 origin/v4.0.1
conda build libclanglite \
            python-clanglite \
            --old-build-string

cd ../../../AutoWIG/bin/conda
conda build python-autowig \
            --old-build-string

set +ve