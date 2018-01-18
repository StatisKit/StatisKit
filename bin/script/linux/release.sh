set -ve

export PY2K=2.7
export PY3K=3.6

source activate
rm -rf ${CONDA_PREFIX}/conda-bld

cd ../../conda
conda build python-scons --python=${PY2K}
conda build python-scons --python=${PY3K}
conda build scons-tools --python=${PY2K}
conda build scons-tools --python=${PY3K}
conda build libtoolchain --python=${PY2K}
conda build libtoolchain --python=${PY3K}
conda build python-toolchain --python=${PY2K}
conda build python-toolchain --python=${PY3K}
conda build boost-suite --python=${PY2K}
conda build boost-suite --python=${PY3K}
conda build boost-meta --python=${PY2K}
conda build boost-meta --python=${PY3K}
conda build python-parse --python=${PY2K}
conda build python-parse --python=${PY3K}

cd ../../share/git/ClangLite/bin/conda
conda build llvm
conda build clang
conda build libclanglite --python=${PY2K}
conda build libclanglite --python=${PY3K}
conda build python-clanglite --python=${PY2K}
conda build python-clanglite --python=${PY3K}

cd ../../../AutoWIG/bin/conda
conda build python-autowig --python=${PY2K}
conda build python-autowig --python=${PY3K}

cd ../../../../../bin/conda
conda build statiskit-dev --python=${PY2K}
conda build statiskit-dev --python=${PY3K}

cd ../script/linux

set +ve