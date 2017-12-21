echo ON

git clone --recursive http://github.com/StatisKit/StatisKit
if errorlevel 1 exit 1

cd StatisKit\bin\conda
if errorlevel 1 exit 1
conda build python-scons ^
            scons-tools ^
            libtoolchain ^
            python-toolchain ^
            boost-suite ^
            boost-meta ^
            python-parse ^
            --old-build-string
if errorlevel 1 exit 1

cd ..\..\share\git\ClangLite\bin\conda
if errorlevel 1 exit 1
conda build llvm ^
            clang ^
            libclanglite ^
            python-clanglite ^
            --old-build-string
if errorlevel 1 exit 1

cd ..\..\..\AutoWIG\bin\conda
if errorlevel 1 exit 1
conda build python-autowig ^
            --old-build-string
if errorlevel 1 exit 1

set +ve