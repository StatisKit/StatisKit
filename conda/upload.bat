echo OFF

DEFAULT_ANACONDA_BUILD_RECIPES=libboost python-scons python-gitpython
DEFAULT_ANACONDA_CHANNELS=statiskit conda-forge
DEFAULT_ANACONDA_CHANNEL=statiskit

if "%ANACONDA_CHANNELS%" == "" (
    set ANACONDA_CHANNELS=%DEFAULT_ANACONDA_CHANNELS%
) else (
    echo "Channels used: "%ANACONDA_CHANNELS%
)

if "%ANACONDA_CHANNEL%" == "" (
    set ANACONDA_CHANNEL=%DEFAULT_ANACONDA_CHANNEL%
) else (
    echo "Channel used: "%ANACONDA_CHANNEL%
)

set ANACONDA_CHANNEL_FLAGS=
for %%ANACONDA_CHANNEL_FLAG in (%ANACONDA_CHANNELS%) do (
    set ANACONDA_CHANNEL_FLAGS=%ANACONDA_CHANNEL_FLAGS% -c %%ANACONDA_CHANNEL_FLAG
)

if "%ANACONDA_BUILD_RECIPES%" == "" (
    set ANACONDA_BUILD_RECIPES=%DEFAULT_ANACONDA_BUILD_RECIPES%
) else (
    echo "Recipes to build: "%ANACONDA_BUILD_RECIPES%
)

if "%ANACONDA_USERNAME%" == "" (
    set /p ANACONDA_USERNAME="Username: "
) else (
    echo Username: %ANACONDA_USERNAME%;
)

if "%ANACONDA_PASSWORD%" == "" (
    set /p ANACONDA_USERNAME=%ANACONDA_USERNAME%%"'s password: "
) else (
    echo %ANACONDA_USERNAME%'s password: [secure];
)

echo ON

conda install -n root anaconda-client
if %errorlevel% neq 0 (
    exit /b %errorlevel%
)

echo OFF

echo y|anaconda login --username %ANACONDA_USERNAME% --password %ANACONDA_PASSWORD%
if %errorlevel% neq 0 (
    exit /b %errorlevel%
)

echo ON

if "%TOOLCHAIN%" == "" (
    git clone https://gist.github.com/c491cb08d570beeba2c417826a50a9c3.git toolchain
    if %errorlevel% neq 0 (
        anaconda logout
        exit /b %errorlevel%
    )
    cd toolchain
    call config.bat
    if %errorlevel% neq 0 (
        cd ..
        anaconda logout
        rmdir toolchain /s /q
        exit /b %errorlevel%
    )
    cd ..
    rmdir toolchain /s /q
)

for %%ANACONDA_BUILD_TARGET in (%ANACONDA_BUILD_TARGETS%) do (
    for /f %%i in ('conda build %%ANACONDA_BUILD_TARGET -c %ANACONDA_CHANNEL_FLAGS% %ANACONDA_BUILD_FLAGS% --output') do set ANACONDA_UPLOAD_RECIPE=%%i
    anaconda upload %ANACONDA_UPLOAD_RECIPE% --user %ANACONDA_CHANNEL% %ANACONDA_UPLOAD_FLAGS%
)

anaconda logout

ECHO OFF