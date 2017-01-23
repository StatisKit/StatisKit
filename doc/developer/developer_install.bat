echo ON

curl http://statiskit.readthedocs.io/en/latest/_downloads/install.bat -o pre-install.bat
call pre-install.bat
rm pre-install.bat

conda update conda-build

echo OFF