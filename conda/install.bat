ECHO ON

conda install python-pkgtk -c statiskit -c conda-forge
if %errorlevel% neq 0 exit /b %errorlevel%