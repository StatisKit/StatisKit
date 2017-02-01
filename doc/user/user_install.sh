if [[ "$BATCH_MODE"="true" ]]; then
    set -v
else
    export BATCH_MODE=false
    set +v
fi

export ERROR=0
export CLEAN_MINICONDA=1

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

if [[ "$ERROR" = "1" ]]; then
    echo "Unknown system"
else
    if [[ "$OS_NAME" = "MacOSX" ]]; then
        PLATFORM=x86_64
        if [[ -f Miniconda2-latest-$OS_NAME-x86_64.sh ]]; then
            export CLEAN_MINICONDA=0
            export CONDA_VERSION=2
        elif [[ -f Miniconda3-latest-$OS_NAME-x86_64.sh ]]; then
            export CLEAN_MINICONDA=0
            export CONDA_VERSION=3
        else
            if [[ "$CONDA_VERSION" = "" ]]; then
                CONDA_VERSION=2
            fi
            curl https://repo.continuum.io/miniconda/Miniconda$CONDA_VERSION-latest-$OS_NAME-$PLATFORM.sh -o Miniconda$CONDA_VERSION-latest-$OS_NAME-$PLATFORM.sh
            if [[ ! "$?" = "0" ]]; then
                export ERROR=1
            fi
        fi
    else
        if [[ "$PLATFORM" = "" ]]; then
            export PLATFORM=`arch`
            if [[ ! "$?" = "0" ]]; then
                export PLATFORM="x86"
            fi
        fi
        if [[ -f Miniconda2-latest-$OS_NAME-$PLATFORM.sh ]]; then
            export CLEAN_MINICONDA=0
            export CONDA_VERSION=2
        elif [[ -f Miniconda3-latest-$OS_NAME-$PLATFORM.sh ]]; then
            export CLEAN_MINICONDA=0
            export CONDA_VERSION=3
        else
            if [[ "$CONDA_VERSION" = "" ]]; then
                export CONDA_VERSION=2
            fi
            wget https://repo.continuum.io/miniconda/Miniconda$CONDA_VERSION-latest-$OS_NAME-$PLATFORM.sh -O Miniconda$CONDA_VERSION-latest-$OS_NAME-$PLATFORM.sh
            if [[ ! "$?" = "0" ]]; then
                export ERROR=1
            fi            
        fi
    fi
    if [[ "$ERROR" = "1" ]]; then
        echo "Download of the Miniconda"$CONDA_VERSION"-latest-"$OS_NAME"-"$PLATFORM".sh file failed"
    else
        if [[ "$CONDA_DIR" = "" ]]; then
            export CONDA_DIR=$HOME/.miniconda$CONDA_VERSION
        fi
        if [[ ! -d "$CONDA_DIR" ]]; then
            if [[ "$BATCH_MODE" = "true" ]]; then
                bash Miniconda$CONDA_VERSION-latest-$OS_NAME-$PLATFORM.sh -p $CONDA_DIR -b
            else
                bash Miniconda$CONDA_VERSION-latest-$OS_NAME-$PLATFORM.sh -p $CONDA_DIR
            fi
            if [[ ! "$?" = "0" ]]; then
                echo "Execution of the Miniconda"$CONDA_VERSION"-latest-"$OS_NAME"-"$PLATFORM".sh file failed"
                export ERROR=1
            fi
        else
            if [[ "$CLEAN_MINICONDA" = "0" ]]; then
                rm Miniconda$CONDA_VERSION-latest-$OS_NAME-$PLATFORM.sh
            fi
        fi
        if [[ "$ERROR" = "0" ]]; then
            if [[ "$CLEAN_MINICONDA" = "1" ]]; then
                rm Miniconda$CONDA_VERSION-latest-$OS_NAME-$PLATFORM.sh
            fi
            export PATH=$CONDA_DIR/bin:$PATH
            if [[ "$CONDA_ALWAYS_YES" = "" ]]; then
              CONDA_ALWAYS_YES=no
            fi
            if [[ "$CONDA_CHANGE_PS1" = "" ]]; then
              CONDA_CHANGE_PS1=yes
            fi
            conda config --set always_yes $CONDA_ALWAYS_YES
            if [[ ! "$?" = "0" ]]; then
                echo "Configuration of Conda failed"
            fi
            conda config --set changeps1 $CONDA_CHANGE_PS1
            if [[ ! "$?" = "0" ]]; then
                echo "Configuration of Conda failed"
            fi
            conda update -q conda -y
            if [[ ! "$?" = "0" ]]; then
                echo "Update of Conda failed"
            fi
            echo "User installation succeded."
        fi
    fi
fi

if [[ "$ERROR" = "1" ]]; then
    echo "User installation failed."
fi 

set +v
