echo ON

git clone https://github.com/StatisKit/Misc.git
if %errorlevel% neq 0 exit /b %errorlevel%

cd Misc/conda
if %errorlevel% neq 0 exit /b %errorlevel%

git clone https://gist.github.com/c491cb08d570beeba2c417826a50a9c3.git config-toolchain
cd config-toolchain
call config.bat
cd ..

conda build libboost -c statiskit -c conda-forge
if %errorlevel% neq 0 exit /b %errorlevel%

conda build python-scons -c statiskit
if %errorlevel% neq 0 exit /b %errorlevel%
