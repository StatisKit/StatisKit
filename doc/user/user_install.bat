echo OFF

if "%CONDA_VERSION%"=="" set CONDA_VERSION=2
if "%CONDA_DIR%"=="" set CONDA_DIR=%USERPROFILE%\Miniconda%CONDA_VERSION%

if "%PLATFORM%"=="" set PLATFORM=%PROCESSOR_ARCHITECTURE%
if not "%PLATFORM%"=="x86" set PLATFORM=x86_64

where curl
if errorlevel 1 (
    if not exist Miniconda%CONDA_VERSION%-latest-Windows-%PLATFORM%.exe (
        echo You must first install the cURL program or download manually the Miniconda%CONDA_VERSION%-latest-Windows-%PLATFORM%.exe file
        goto :failure
    )
)

if "%BATCH_MODE%"=="" set BATCH_MODE=false

if not exist %CONDA_DIR% (
    if exist Miniconda%CONDA_VERSION%-latest-Windows-%PLATFORM%.exe (
        set CLEAN_MINICONDA=0
    ) else (
        curl https://repo.continuum.io/miniconda/Miniconda%CONDA_VERSION%-latest-Windows-%PLATFORM%.exe -o miniconda.exe
        set CLEAN_MINICONDA=1
    )
    if errorlevel 1 (
        echo Download of the Miniconda"%CONDA_VERSION%"-latest-Windows-"%PLATFORM%".exe file failed
        goto :failure
    )
    if "%BATCH_MODE%"=="true" (
        start /wait "" miniconda.exe /InstallationType=JustMe /RegisterPython=0 /S /D=%CONDA_DIR%
    ) else (
        start /wait "" miniconda.exe /InstallationType=JustMe /RegisterPython=0 /D=%CONDA_DIR%
    )
    if errorlevel 1 (
        echo Execution of the Miniconda"%CONDA_VERSION%"-latest-Windows-"%PLATFORM%".exe file failed
        goto :failure
    )
    if "%CLEAN_MINICONDA%"=="1" del miniconda.exe
)

attrib +h %CONDA_DIR%
if errorlevel 1 echo Failed to hide the "%CONDA_DIR%" directory

set PATH=%CONDA_DIR%;%CONDA_DIR%\Scripts;%PATH%
call %CONDA_DIR%\Scripts\activate.bat root
if errorlevel 1 (
    echo Activation of Conda failed
    goto :failure
)

if "%CONDA_ALWAYS_YES%"=="" set CONDA_ALWAYS_YES=no
if "%CONDA_CHANGE_PS1%"=="" set CONDA_CHANGE_PS1=yes

conda config --set always_yes %CONDA_ALWAYS_YES%
if errorlevel 1 (
    echo Configuration of Conda failed
    goto :failure
)
conda config --set changeps1 %CONDA_CHANGE_PS1%
if errorlevel 1 (
    echo Configuration of Conda failed
    goto :failure
)
conda update -q conda -y
if errorlevel 1 (
    echo Update of Conda failed
    goto :failure
)

echo User installation succeded.

echo OFF

:failure
    echo User installation failed.
    echo OFF