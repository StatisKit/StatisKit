echo OFF

set DEFAULT_ANACONDA_INSTALL_RECIPES=libboost
set DEFAULT_ANACONDA_CHANNELS=statiskit conda-forge
set DEFAULT_ANACONDA_INSTALL_FLAGS=--use-local

if "%ANACONDA_CHANNELS%" == "" (
    set ANACONDA_CHANNELS=%DEFAULT_ANACONDA_CHANNELS%
) else (
    echo "Channels used: "%ANACONDA_CHANNELS%
)

set ANACONDA_CHANNEL_FLAGS=
for %%ANACONDA_CHANNEL_FLAG in (%ANACONDA_CHANNELS%) do (
    set ANACONDA_CHANNEL_FLAGS=%ANACONDA_CHANNEL_FLAGS% -c %%ANACONDA_CHANNEL_FLAG
)

if "%ANACONDA_INSTALL_RECIPES%" == "" (
    set ANACONDA_INSTALL_RECIPES=%DEFAULT_ANACONDA_INSTALL_RECIPES%
) else (
    echo "Recipes to build: "%ANACONDA_INSTALL_RECIPES%
)

if "%ANACONDA_INSTALL_FLAGS%" == "" (
    set ANACONDA_INSTALL_FLAGS=%DEFAULT_ANACONDA_INSTALL_FLAGS%
)

echo ON

for %%i in (%ANACONDA_INSTALL_RECIPES%) do (
  conda install %%i --use-local %ANACONDA_CHANNEL_FLAGS% %ANACONDA_INSTALL_FLAGS%
  if %errorlevel% neq 0 (
    exit /b %errorlevel%
  )
)

ECHO OFF