SETLOCAL

dir C:\Program Files (x86)
CALL cl /v
exit /b 0

CALL conda build toolchain -c statiskit -c conda-forge
IF %errorlevel% neq 0 exit /b %errorlevel%
CALL conda build boost_build -c statiskit -c conda-forge
IF %errorlevel% neq 0 exit /b %errorlevel%
CALL conda build libboost_python -c statiskit -c conda-forge
if %errorlevel% neq 0 exit /b %errorlevel%
CALL conda build python-scons -c statiskit
IF %errorlevel% neq 0 exit /b %errorlevel%
CALL conda build python-parse -c statiskit
IF %errorlevel% neq 0 exit /b %errorlevel%

IF NOT "%APPVEYOR_REPO_BRANCH%"=="master" GOTO DONE
IF "%ANACONDA_USERNAME%"=="" GOTO DONE
IF "%ANACONDA_PASSWORD%"=="" GOTO DONE

CALL conda install -n root anaconda-client
if %errorlevel% neq 0 exit /b %errorlevel%

anaconda login --username "%ANACONDA_USERNAME%" --password "%ANACONDA_PASSWORD%" --hostname "AppVeyor%APPVEYOR_BUILD_NUMBER%" 
IF %errorlevel% neq 0 exit /b %errorlevel%

::FOR %%CONDA_RECIPE IN (toolchain, python-scons, python-parse) DO (
::  ECHO %%CONDA_RECIPE
  
FOR /f %%i in ('conda build toolchain --output') DO (set CONDA_FILE=%%i)
CALL anaconda upload --user statiskit %CONDA_FILE% --force
IF %errorlevel% neq 0 exit /b %errorlevel%

FOR /f %%i in ('conda build python-scons --output') DO (set CONDA_FILE=%%i)
CALL anaconda upload --user statiskit %CONDA_FILE% --force
IF %errorlevel% neq 0 exit /b %errorlevel%

FOR /f %%i in ('conda build python-parse --output') DO (set CONDA_FILE=%%i)
CALL anaconda upload --user statiskit %CONDA_FILE% --force
IF %errorlevel% neq 0 exit /b %errorlevel%

CALL anaconda logout
GOTO DONE

:DONE
ECHO ~~~~~~~~~~~~~~~~~~~~~~ DONE %~f0 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
