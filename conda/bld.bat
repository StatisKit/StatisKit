ECHO ON

git clone https://github.com/pfernique/PkgTk.git
if %errorlevel% neq 0 exit /b %errorlevel%
cd PkgTk\conda
if %errorlevel% neq 0 exit /b %errorlevel%

conda build conda/python-pkgtk -c statiskit -c conda-forge
if %errorlevel% neq 0 exit /b %errorlevel%