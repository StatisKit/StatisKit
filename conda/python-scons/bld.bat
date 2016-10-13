echo ON

"%PYTHON%" setup.py install --standard-lib
if errorlevel 1 exit 1
