echo ON

git clone https://github.com/StatisKit/Misc.git
if %errorlevel% neq 0 exit /b %errorlevel%

cd Misc/conda
if %errorlevel% neq 0 exit /b %errorlevel%

conda install python-pkgtk -c statiskit -c conda-forge
if %errorlevel% neq 0 exit /b %errorlevel%

for /f %%i in ('pkgtk toolchain') DO (set TOOLCHAIN=%%i)
if %errorlevel% neq 0 exit /b %errorlevel%

conda build libboost -c statiskit -c conda-forge
if %errorlevel% neq 0 exit /b %errorlevel%

conda build python-scons -c statiskit
if %errorlevel% neq 0 exit /b %errorlevel%