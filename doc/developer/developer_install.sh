set +v

export ERROR=0

case "$(uname -s)" in

    Darwin)
        export OS_NAME=MacOSX
        ;;

    Linux)
        export OS_NAME=Linux
        ;;

    *)
        export ERROR=1
        ;;

esac

export CLEAN_INSTALL=1
if [[ ! -f user_install.sh && "$ERROR" = "0" ]]; then
    if [[ "$OS_NAME" = "MacOSX" ]]; then
        curl https://raw.githubusercontent.com/StatisKit/StatisKit/master/doc/user/user_install.sh -o user_install.sh
    else
        wget https://raw.githubusercontent.com/StatisKit/StatisKit/master/doc/user/user_install.sh -O user_install.sh
    fi
    if [[ ! "$?" = "0" ]]; then
        echo "Download of the user_install.sh file for Conda installation failed."
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
if [[ "$ERROR" = "0" ]]; then
    if [[ "$%CONFIGURE_ONLY%" = "" ]]; then
        export CONFIGURE_ONLY="false"
    fi
    if [[ "$%CONFIGURE_ONLY%" = "false" ]]; then
        if [[ "$%STATISKIT_DEV%" = "" ]]; then
            conda env update statiskit/statiskit-dev
            if [[ ! "$?" = "0" ]]; then
                export ERROR=1
            fi
        else
            conda env update statiskit/statiskit-dev -n $%STATISKIT_DEV%
            if [[ ! "$?" = "0" ]]; then
                export ERROR=1
            fi
        fi
    fi
fi

if [[ "$ERROR" = "0" ]]; then
    if [[ ! "$CONFIGURE_ONLY" = "false" ]]; then
        echo "Developer configuration succeded."
    else
        echo "Developer configuration and installation succeded."
    fi
else
    echo "Developer configuration failed."
else

set +v
