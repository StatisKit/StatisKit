echo ON

git clone https://github.com/StatisKit/Misc.git
if %errorlevel% neq 0 exit /b %errorlevel%

cd Misc/conda
if %errorlevel% neq 0 exit /b %errorlevel%

echo OFF

if "%BUILD_TARGETS%" == "" set BUILD_TARGETS="libboost python-scons"

echo ON

git clone https://gist.github.com/c491cb08d570beeba2c417826a50a9c3.git toolchain
cd toolchain
call config.bat
cd ..
rmdir toolchain /s /q

for %%BUILD_TARGET in (%BUILD_TARGETS%) do (
    conda build %%BUILD_TARGET -c statiskit
    if %errorlevel% neq 0 exit /b %errorlevel%
)