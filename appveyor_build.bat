SETLOCAL

conda build toolchain -c statiskit
conda create -n _appveyor toolchain --use-local
activate _appveyor
conda build libboost-python -c statiskit
conda build python-scons -c statiskit
conda build python-parse -c statiskit

IF NOT "%APPVEYOR_REPO_BRANCH%"=="master" GOTO DONE
IF "%ANACONDA_USERNAME%"=="" GOTO DONE
IF "%ANACONDA_PASSWORD%"=="" GOTO DONE

conda install anaconda-client;
anaconda login --username "%ANACONDA_USERNAME%" --password "%ANACONDA_PASSWORD%"

FOR %%CONDA_RECIPE IN (toolchain, python-scons, python-parse) DO (
  FOR /f %%i in ('conda build %CONDA_RECIPE% --output') DO (set CONDA_FILE=%%i)
  anaconda upload --user statiskit %CONDA_FILE% --force;
)
        
GOTO DONE

:DONE
ECHO ~~~~~~~~~~~~~~~~~~~~~~ DONE %~f0 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
