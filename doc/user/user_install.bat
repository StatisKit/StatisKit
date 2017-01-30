setlocal EnableDelayedExpansion

echo ON

if "%CONDA_VERSION%"=="" set CONDA_VERSION=2
if "%CONDA_DIR%"=="" set CONDA_DIR=%USERPROFILE%\Miniconda!CONDA_VERSION!

if "%PLATFORM%"=="" set PLATFORM=%PROCESSOR_ARCHITECTURE%
if not "!PLATFORM!"=="x86" set PLATFORM=x86_64

where curl
if !ERRORLEVEL! neq 0 (
    echo "You must first install the cURL program"
    exit /b !ERRORLEVEL!
)

if "%BATCH_MODE%"=="" set BATCH_MODE=false

if not exist !CONDA_DIR! (
    curl https://repo.continuum.io/miniconda/Miniconda!CONDA_VERSION!-latest-Windows-!PLATFORM!.exe -o miniconda.exe
    if !ERRORLEVEL! neq 0 exit /b !ERRORLEVEL!
    if "%BATCH_MODE%"=="true" (
        start /wait "" miniconda.exe /InstallationType=JustMe /RegisterPython=0 /S /D=!CONDA_DIR!
    ) else (
        start /wait "" miniconda.exe /InstallationType=JustMe /RegisterPython=0 /D=!CONDA_DIR!
    )
    if !ERRORLEVEL! neq 0 exit /b !ERRORLEVEL!
    del miniconda.exe
    if !ERRORLEVEL! neq 0 exit /b !ERRORLEVEL!
)

attrib +h !CONDA_DIR!
if !ERRORLEVEL! neq 0 echo Failed to hide the !CONDA_DIR! directory

set PATH=!CONDA_DIR!;!CONDA_DIR!\Scripts;%PATH%

if "%CONDA_ALWAYS_YES%"=="" set CONDA_ALWAYS_YES=no
if "%CONDA_CHANGE_PS1%"=="" set CONDA_CHANGE_PS1=yes

conda config --set always_yes !CONDA_ALWAYS_YES!
if !ERRORLEVEL! neq 0 exit /b !ERRORLEVEL!
conda config --set changeps1 !CONDA_CHANGE_PS1!
if !ERRORLEVEL! neq 0 exit /b !ERRORLEVEL!
conda update -q conda
if !ERRORLEVEL! neq 0 exit /b !ERRORLEVEL!

echo OFF
