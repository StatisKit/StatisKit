echo ON

conda build toolchain -c statiskit -c conda-forge
if %errorlevel% neq 0 exit /b %errorlevel%
conda install toolchain --use-local -c statiskit -c conda-forge
if %errorlevel% neq 0 exit /b %errorlevel%
activate %CONDA_DEFAULT_ENV%
if %errorlevel% neq 0 exit /b %errorlevel%

:: conda build boost_build -c statiskit -c conda-forge
:: if %errorlevel% neq 0 exit /b %errorlevel%
:: conda install boost_build --use-local -c statiskit -c conda-forge
:: if %errorlevel% neq 0 exit /b %errorlevel%

conda build libboost_python -c statiskit -c conda-forge
if %errorlevel% neq 0 exit /b %errorlevel%
conda install libboost_python --use-local -c statiskit -c conda-forge
if %errorlevel% neq 0 exit /b %errorlevel%

conda build python-scons -c statiskit
if %errorlevel% neq 0 exit /b %errorlevel%
conda install python-scons --use-local -c statiskit -c conda-forge
if %errorlevel% neq 0 exit /b %errorlevel%

conda build python-parse -c statiskit
if %errorlevel% neq 0 exit /b %errorlevel%
conda install python-parse --use-local -c statiskit -c conda-forge
if %errorlevel% neq 0 exit /b %errorlevel%
