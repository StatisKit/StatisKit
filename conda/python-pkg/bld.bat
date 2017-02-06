echo ON

python setup.py install --prefix=%PREFIX%
if errorlevel 1 exit 1

echo OFF
