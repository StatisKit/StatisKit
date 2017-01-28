set +v

export CLEAN_INSTALL=1
if [[ ! -f install.sh ]]; then
    wget http://statiskit.readthedocs.io/en/latest/_downloads/user_install.sh -O user_install.sh
    if [[ ! "$?" = "0" ]]; then
        echo "Download of the user_install.sh file for Conda installation failed"
        export ERROR=1
    else
        export ERROR=0
    fi
else
    export ERROR=0
    export CLEAN_INSTALL=0
fi

if [[ "$ERROR" = "0" ]]; then
    source user_install.sh
    if [[ "$CLEAN_INSTALL" = "1" ]]; then
        rm user_install.sh
    fi
    if [[ "$ERROR" = "0" ]]; then
        python -c "import conda_build" >/dev/null 2>/dev/null  
        if [[ ! "$?" = "0" ]]; then
            conda install -n root conda-build -y
        else
            conda update -n root conda-build -y
        fi
        python -c "import binstar_client" >/dev/null 2>/dev/null  
        if [[ ! "$?" = "0" ]]; then
            conda install -n root anaconda-client -y
        else
            conda update -n root anaconda-client -y
        fi
    fi
fi
if [[ "$ERROR" = "1" ]]; then
    echo "Developer configuration failed."
else
    if [[ "$ENVIRONMENT" = "" ]]; then
        conda env update statiskit/statiskit-dev
        if [[ ! "$?" = "0" ]]; then
            export ERROR=1
        fi
    else
        conda env update statiskit/statiskit-dev -n $ENVIRONMENT
        if [[ ! "$?" = "0" ]]; then
            export ERROR=1
        fi
    fi
fi

if [[ "$ERROR" = "0" ]]; then
    echo "Developer configuration succeded."
fi

set +v