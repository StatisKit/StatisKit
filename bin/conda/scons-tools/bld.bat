echo ON

if not exist %PREFIX%\etc\conda\activate.d mkdir %PREFIX%\etc\conda\activate.d
copy %RECIPE_DIR%\activate.bat %PREFIX%\etc\conda\activate.d\statiskit_scons_vars.sh

if not exist %PREFIX%\etc\conda\activate.d mkdir %PREFIX%\etc\conda\deactivate.d
copy %RECIPE_DIR%\deactivate.bat %PREFIX%\etc\conda\deactivate.d\statiskit_scons_vars.sh

set TGT_DIR=scons_tools
mkdir %SP_DIR%\%TGT_DIR%
type NUL > %SP_DIR%\%TGT_DIR%\__init__.py
set TGT_DIR=%TGT_DIR%\site_tools
mkdir %SP_DIR%\%TGT_DIR%
type NUL > %SP_DIR%\%TGT_DIR%\__init__.py

for /r %%i in (*) do (
    if "%PY3K%" == "1" (
        2to3 -n -w %%i
    )
    copy %%i %SP_DIR%/%TGT_DIR%/%%i
)

echo OFF