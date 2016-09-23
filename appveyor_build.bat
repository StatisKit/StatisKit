SETLOCAL

CALL conda build toolchain -c statiskit
if %errorlevel% neq 0 exit /b %errorlevel%
CALL conda create -n _appveyor toolchain --use-local
if %errorlevel% neq 0 exit /b %errorlevel%
CALL activate _appveyor
if %errorlevel% neq 0 exit /b %errorlevel%
:: CALL conda build libboost-python -c statiskit
:: if %errorlevel% neq 0 exit /b %errorlevel%
CALL conda build python-scons -c statiskit
if %errorlevel% neq 0 exit /b %errorlevel%
CALL conda build python-parse -c statiskit
if %errorlevel% neq 0 exit /b %errorlevel%

IF NOT "%APPVEYOR_REPO_BRANCH%"=="master" GOTO DONE
IF "%ANACONDA_USERNAME%"=="" GOTO DONE
IF "%ANACONDA_PASSWORD%"=="" GOTO DONE

CALL conda install -n root anaconda-client
if %errorlevel% neq 0 exit /b %errorlevel%
CALL anaconda login --username "%ANACONDA_USERNAME%" --password "%ANACONDA_PASSWORD%"
if %errorlevel% neq 0 exit /b %errorlevel%

FOR %%CONDA_RECIPE IN (toolchain, python-scons, python-parse) DO (
  ECHO %CONDA_RECIPE%
  FOR /f %%i in ('conda build %CONDA_RECIPE% --output') DO (set CONDA_FILE=%%i)
  CALL anaconda upload --user statiskit %CONDA_FILE% --force;
  if %errorlevel% neq 0 exit /b %errorlevel%
)
        
GOTO DONE

:DONE
ECHO ~~~~~~~~~~~~~~~~~~~~~~ DONE %~f0 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
