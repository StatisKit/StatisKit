set +v

if [[ "$ERROR" = "1" ]]; then
    export CLEAN_ENVIRONMENT="false"
else
    export CLEAN_ENVIRONMENT="true"
fi

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

if [[ "$CLEAN_INSTALL" = "" ]]; then
    export CLEAN_INSTALL=1
fi
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
    if [[ "$CONFIGURE_ONLY" = "" ]]; then
        export CONFIGURE_ONLY="false"
    fi
    if [[ "$CONFIGURE_ONLY" = "false" ]]; then
        if [[ "$STATISKIT_DEV" = "" ]]; then
            export STATISKIT_DEV=statiskit-dev
        fi
        if [[ "$CLEAN_ENVIRONMENT" = "true" ]]; then
            conda env remove -y -n $STATISKIT_DEV >/dev/null 2>/dev/null 
        fi
        conda install ipython jupyter ipdb -n $STATISKIT_DEV -y -m -c statiskit -c conda-forge
        GIT=`which git`
        if [[ "$GIT" = "" ]]; then
            conda install git -n $STATISKIT_DEV -y
            if [[ ! "$?" = "0" ]]; then
                export ERROR="1"
            fi
            source activate $STATISKIT_DEV
        fi
        if [[ -d StatisKit && "$CLEAN_STATISKIT" = "" ]]; then
            export CLEAN_STATISKIT=false
        else
            export CLEAN_STATISKIT=true
            git clone https://github.com/StatisKit/StatisKit.git
            if [[ ! "$?" = "0" ]]; then
                echo "Clone of the StatisKit repository failed." 
                export ERROR=1
            fi
        fi
        if [[ "$ERROR" = "0" ]]; then
            cd StatisKit
            conda build conda/python-scons -c statiskit -c conda-forge
            if [[ ! "$?" = "0" ]]; then
                echo "Build of the python-scons Conda recipe failed."
                cd ..
                export ERROR=1
            else
                conda install -n $STATISKIT_DEV python-scons --use-local -c statiskit -c conda-forge -y
                if [[ ! "$?" = "0" ]]; then
                    echo "Creation of the StatisKit development environment failed."
                    cd ..
                    export ERROR=1
                else
                    source activate $STATISKIT_DEV
                    if [[ ! "$?" = "0" ]]; then
                        echo "Activation of the StatisKit development environment failed."
                        cd ..
                        export ERROR=1
                    else
                        scons conda-install
                        if [[ ! "$?" = "0" ]]; then
                            echo "Installation of the StatisKit development environment failed."
                            export ERROR=1
                        fi
                        cd ..
                    fi
                fi
            fi
        fi
        if [[ "$ERROR" = "0" ]]; then
            if [[ -d PyClangLite && "$CLEAN_PYCLANGLITE" = "" ]]; then
                export CLEAN_PYCLANGLITE=false
            else
                export CLEAN_PYCLANGLITE=true
                git clone https://github.com/StatisKit/PyClangLite.git
                if [[ ! "$?" = "0" ]]; then
                    echo "Clone of the PyClangLite repository failed." 
                    export ERROR=1
                fi
            fi
            if [[ "$ERROR" = "0" ]]; then
                cd PyClangLite
                scons conda-install
                if [[ ! "$?" = "0" ]]; then
                    echo "Installation of PyClangLite in the development environment failed."
                    export ERROR=1
                fi
                cd ..
            fi
        fi
        if [[ "$ERROR" = "0" ]]; then
            if [[ -d AutoWIG && "$CLEAN_AUTOWIG" = "" ]]; then
                export CLEAN_AUTOWIG=false
            else
                export CLEAN_AUTOWIG=true
                git clone https://github.com/StatisKit/AutoWIG.git
                if [[ ! "$?" = "0" ]]; then
                    echo "Clone of the AutoWIG repository failed." 
                    export ERROR=1
                fi
            fi
            if [[ "$ERROR" = "0" ]]; then
                cd AutoWIG
                scons conda-install
                if [[ ! "$?" = "0" ]]; then
                    echo "Installation of AutoWIG in the development environment failed."
                    export ERROR=1
                fi
                cd ..
            fi
        fi
    fi
fi
    
if [[ "$ERROR" = "0" ]]; then
    conda build purge
    if [[ ! "$CONFIGURE_ONLY" = "false" ]]; then
        echo "Developer configuration succeded."
    else
        echo "Developer configuration and installation succeded."
    fi
else
    echo "Developer configuration failed."
fi

set +v
