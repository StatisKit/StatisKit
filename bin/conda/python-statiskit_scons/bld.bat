echo ON

if not exist %PREFIX%\etc\conda\activate.d mkdir %PREFIX%\etc\conda\activate.d
copy %RECIPE_DIR%\activate.bat %PREFIX%\etc\conda\activate.d\statiskit_scons_vars.sh

if not exist %PREFIX%\etc\conda\activate.d mkdir %PREFIX%\etc\conda\deactivate.d
copy %RECIPE_DIR%\deactivate.bat %PREFIX%\etc\conda\activate.d\statiskit_scons_vars.sh

mkdir $SP_DIR\statiskit_scons
type NUL > %SP_DIR%\statiskit_scons\__init__.py

for /r %%i in (*) do (
    if "%PY3K%" == "1" (
        2to3 -n -w %%i
    )
    copy %%i %SP_DIR%/statiskit_scons/%%i
)

echo OFF