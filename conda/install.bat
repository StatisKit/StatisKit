echo ON

conda install ipython jupyter
if %errorlevel% neq 0 exit /b %errorlevel%

conda install libboost --use-local -c statiskit
if %errorlevel% neq 0 exit /b %errorlevel%

conda install python-scons --use-local -c statiskit
if %errorlevel% neq 0 exit /b %errorlevel%