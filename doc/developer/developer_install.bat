echo OFF

where curl
if errorlevel 1 (
    if not exist user_install.bat (
        echo "You must first install the cURL program or download manually the user_install.bat file"
        exit 1
    )
)

if exist user_install.bat (
    set CLEAN_INSTALL=0
) else (
    set CLEAN_INSTALL=1
)
if not exist user_install.bat curl https://raw.githubusercontent.com/StatisKit/StatisKit/master/doc/user/user_install.bat -o user_install.bat
if errorlevel 1 (
    echo "Download of the user_install.bat file for Conda installation failed."
    echo "Developer configuration failed."
    exit 1
)
call user_install.bat
if errorlevel 1 exit 1
if "%CLEAN_INSTALL%"=="1" del user_install.bat

python -c "import conda_build" >nul 2>nul
if errorlevel 1 (
    conda install -n root conda-build -y
) else (
    conda update -n root conda-build -y
)
python -c "import binstar_client" >nul 2>nul  
if errorlevel 1 (
    conda install -n root anaconda-client -y
) else (
    conda update -n root anaconda-client -y
)

if "%ENVIRONMENT%"== "" (
    conda env update statiskit/statiskit-dev
    if errorlevel 1 (
        echo "Installation of the development environment failed." 
        echo "Developer configuration failed."
        exit 1
    ) else (
        echo "Developer configuration succeded."
    )
) else (
    conda env update statiskit/statiskit-dev -n %ENVIRONMENT%
    if errorlevel 1 (
        echo "Installation of the development environment failed." 
        echo "Developer configuration failed."
        exit 1
    ) else (
        echo "Developer configuration succeded."
    )
)

echo OFF