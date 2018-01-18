echo ON

set PY2K=2.7
set PY3K=3.6

rmdir %CONDA_PREFIX%\conda-bld /S /q

cd ..\..\bin\conda
if errorlevel 1 exit 1
conda build python-scons --python=%PY2K%
if errorlevel 1 exit 1
conda build python-scons --python=%PY3K%
if errorlevel 1 exit 1
conda build scons-tools --python=%PY2K%
if errorlevel 1 exit 1
conda build scons-tools --python=%PY3K%
if errorlevel 1 exit 1
conda build libtoolchain --python=%PY2K%
if errorlevel 1 exit 1
conda build libtoolchain --python=%PY3K%
if errorlevel 1 exit 1
conda build python-toolchain --python=%PY2K%
if errorlevel 1 exit 1
conda build python-toolchain --python=%PY3K%
if errorlevel 1 exit 1
conda build boost-suite --python=%PY2K%
if errorlevel 1 exit 1
conda build boost-suite --python=%PY3K%
if errorlevel 1 exit 1
conda build boost-meta --python=%PY2K%
if errorlevel 1 exit 1
conda build boost-meta --python=%PY3K%
if errorlevel 1 exit 1
conda build python-parse --python=%PY2K%
if errorlevel 1 exit 1
conda build python-parse --python=%PY3K%
if errorlevel 1 exit 1

cd ..\..\share\git\ClangLite\bin\conda
if errorlevel 1 exit 1
conda build llvm
if errorlevel 1 exit 1
conda build clang
if errorlevel 1 exit 1
conda build libclanglite --python=%PY2K%
if errorlevel 1 exit 1
conda build libclanglite --python=%PY3K%
if errorlevel 1 exit 1
conda build python-clanglite --python=%PY2K%
if errorlevel 1 exit 1
conda build python-clanglite --python=%PY3K%
if errorlevel 1 exit 1

cd ..\..\..\AutoWIG\bin\conda
if errorlevel 1 exit 1
conda build python-autowig --python=%PY2K%
if errorlevel 1 exit 1
conda build python-autowig --python=%PY3K%
if errorlevel 1 exit 1

cd ..\..\..\..\..\bin\conda
if errorlevel 1 exit 1

conda build statiskit-dev --python=%PY2K%
if errorlevel 1 exit 1
conda build statiskit-dev --python=%PY3K%
if errorlevel 1 exit 1

cd ..\script\win

echo OFF