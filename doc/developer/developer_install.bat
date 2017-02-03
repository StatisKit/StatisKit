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

if "%CONFIGURE_ONLY%"=="" set CONFIGURE_ONLY="false"

if "%CONFIGURE_ONLY%"=="false" (
    if "%STATISKIT_DEV%"== "" set STATISKIT_DEV=statiskit-dev
    git clone https://github.com/StatisKit/StatisKit.git
    if errorlevel 1 (
        echo "Clone of the StatisKit repository failed." 
        echo "Developer configuration failed."
        exit 1
    )
    cd StatisKit
    conda build conda/python-scons -c statiskit -c conda-forge
    if errorlevel 1 (
        echo "Build of the python-scons Conda recipe failed." 
        echo "Developer configuration failed."
        exit 1
    )
    conda create -n %STATISKIT_DEV% python-scons
    if errorlevel 1 (
        echo "Creation of the StatisKit development environment failed." 
        echo "Developer configuration failed."
        exit 1
    )
    activate %STATISKIT_DEV%
    if errorlevel 1 (
        echo "Activation of the StatisKit development environment failed." 
        echo "Developer configuration failed."
        exit 1
    )
    scons
    if errorlevel 1 (
        echo "Installation of the development environment failed." 
        echo "Developer configuration failed."
        exit 1
    ) else (
        echo "Developer configuration and installation succeded."
    )
) else (
    echo "Developer configuration succeded."
)

echo OFF
