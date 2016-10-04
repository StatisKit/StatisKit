ECHO ON

conda install python-parse --use-local -c statiskit -c conda-forge
if %errorlevel% neq 0 exit /b %errorlevel%
conda install python-pkgtk --use-local -c statiskit -c conda-forge
if %errorlevel% neq 0 exit /b %errorlevel%