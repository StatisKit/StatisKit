echo ON

:: activate
:: if errorlevel 1 exit 1
rmdir %CONDA_PREFIX%\conda-bld\ /S /q

cd ..\..\conda
if errorlevel 1 exit 1
conda build python-scons ^
            scons-tools ^
            libtoolchain ^
            python-toolchain ^
            boost-suite ^
            boost-meta ^
            python-parse
if errorlevel 1 exit 1

cd ..\..\share\git\ClangLite\bin\conda
if errorlevel 1 exit 1
conda build llvm ^
            clang ^
            libclanglite ^
            python-clanglite
if errorlevel 1 exit 1

cd ..\..\..\AutoWIG\bin\conda
if errorlevel 1 exit 1
conda build python-autowig
if errorlevel 1 exit 1

cd ..\..\..\..\..\bin\conda
if errorlevel 1 exit 1

conda build statiskit-dev

cd ..\script\win

echo OFF