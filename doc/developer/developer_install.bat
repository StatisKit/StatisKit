echo OFF

if "%ERROR%"=="1" (
    set CLEAN_ENVIRONMENT=false
) else (
    set CLEAN_ENVIRONMENT=true
)

set ERROR=0

where curl
if errorlevel 1 (
    if not exist user_install.bat (
        echo You must first install the cURL program or download manually the user_install.bat file
        goto :failure
    )
)

if exist user_install.bat (
    set CLEAN_INSTALL=0
) else (
    set CLEAN_INSTALL=1
)
if not exist user_install.bat curl https://raw.githubusercontent.com/StatisKit/StatisKit/master/doc/user/user_install.bat -o user_install.bat
if errorlevel 1 (
    echo Download of the user_install.bat file for Conda installation failed.
    goto :failure
)
call user_install.bat
if errorlevel 1 goto :failure
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

if "%CONFIGURE_ONLY%"=="" set CONFIGURE_ONLY=false

if "%CONFIGURE_ONLY%"=="false" (
    if "%STATISKIT_DEV%"== "" set STATISKIT_DEV=statiskit-dev
    if "%CLEAN_ENVIRONMENT%"=="true" (
        conda env remove -y -n %STATISKIT_DEV% >nul 2>nul
    )
    conda install ipython jupyter -n %STATISKIT_DEV% -y -m -c statiskit -c conda-forge
    where git
    if errorlevel 1 (
        conda install git -n %STATISKIT_DEV% -y
        if errorlevel 1 (
            echo installation of git failed.
            goto :failure
        )
        activate %STATISKIT_DEV%
    )
    git clone https://github.com/StatisKit/StatisKit.git
    if errorlevel 1 (
        echo Clone of the StatisKit repository failed.
        goto :failure
    )
    cd StatisKit
    conda build conda/python-scons -c statiskit -c conda-forge
    if errorlevel 1 (
        echo Build of the python-scons Conda recipe failed.
        goto :failure
    )
    echo y|conda install -n %STATISKIT_DEV% python-scons --use-local -c statiskit -c conda-forge -y
    if errorlevel 1 (
        echo Creation of the StatisKit development environment failed.
        goto :failure
    )
    activate %STATISKIT_DEV%
    if errorlevel 1 (
        echo Activation of the StatisKit development environment failed.
        goto :failure
    )
    scons conda-install
    if errorlevel 1 (
        cd ..
        echo Installation of the development environment failed.
        goto :failure
    )
    cd ..
    git clone https://github.com/StatisKit/ClangLite.git
    if errorlevel 1 (
        echo Clone of the ClangLite repository failed.
        goto :failure
    )
    cd PyClangLite
    scons conda-install
    if errorlevel 1 (
        cd ..
        echo Installation of the development environment failed.
        goto :failure
    )
    cd ..
    git clone https://github.com/StatisKit/AutoWIG.git
    if errorlevel 1 (
        echo Clone of the AutoWIG repository failed.
        goto :failure
    )
    cd AutoWIG
    scons conda-install
    if errorlevel 1 (
        cd ..
        echo Installation of the development environment failed.
        goto :failure
    ) else (
        cd ..
        echo Developer configuration and installation succeded.
    )
) else (
    echo Developer configuration succeded.
)

echo OFF

:failure
    set ERROR=1
    echo Developer configuration failed.
    echo OFF