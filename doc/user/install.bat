setlocal EnableDelayedExpansion

echo ON

if "%CONDA_VERSION%"=="" set CONDA_VERSION=2
if "%CONDA_DIR%"=="" set CONDA_DIR='%USERPROFILE%\Miniconda!CONDA_VERSION!'

if "%PLATFORM%"=="" set PLATFORM=%PROCESSOR_ARCHITECTURE%
if not "!PLATFORM!"=="x86" set PLATFORM=x86_64

where curl
if !ERRORLEVEL! neq 0 (
    echo "You must first install the cURL program"
    exit /b !ERRORLEVEL!
)

if not exist %CONDA_DIR% (
    curl https://repo.continuum.io/miniconda/Miniconda%CONDA_VERSION%-latest-Windows-%PLATFORM%.exe -o miniconda.exe
    if !ERRORLEVEL! neq 0 exit /b !ERRORLEVEL!
    start /wait "" miniconda.exe /InstallationType=JustMe /RegisterPython=0 /S /D=%CONDA_DIR%
    if !ERRORLEVEL! neq 0 exit /b !ERRORLEVEL!
    del miniconda.exe
    if !ERRORLEVEL! neq 0 exit /b !ERRORLEVEL!
)

set PATH=%CONDA_DIR%;%CONDA_DIR%\Scripts;%PATH%

if [[ "$CONDA_ALWAYS_YES" = "" ]]; then
  CONDA_ALWAYS_YES=no
fi
if [[ "$CONDA_CHANGE_PS1" = "" ]]; then
  CONDA_CHANGE_PS1=yes
fi
conda config --set always_yes $CONDA_ALWAYS_YES
if !ERRORLEVEL! neq 0 exit /b !ERRORLEVEL!
conda config --set changeps1 $CONDA_CHANGE_PS1
if !ERRORLEVEL! neq 0 exit /b !ERRORLEVEL!
conda update -q conda
if !ERRORLEVEL! neq 0 exit /b !ERRORLEVEL!

echo OFF
