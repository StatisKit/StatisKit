set +v

export CLEAN_INSTALL=1
if [[ ! -f install.sh ]]; then
    wget http://statiskit.readthedocs.io/en/latest/_downloads/user_install.sh -O user_install.sh
    if [[ ! "$?" = "0" ]]; then
        echo "Download of the user_install.sh file failed"
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
    else
        conda env update statiskit/statiskit-dev -n $ENVIRONMENT
    fi
    if [[ -d "$HOME/.config/sublime-text-3" ]]; then
        export SUBLIME_TEXT=3
    elif [[ -d "$HOME/.config/sublime-text-2" ]]; then
        export SUBLIME_TEXT=2
    fi
    if [[ ! "$SUBLIME_TEXT" = "" ]]; then
        python -c "import mako" >/dev/null 2>/dev/null
        if [[ "$?" = "0" ]]; then
            export REMOVE_MAKO=0
        else
            export REMOVE_MAKO=1
            conda install mako -c conda-forge -y
        fi        
        wget https://raw.githubusercontent.com/StatisKit/StatisKit/master/doc/developper/SCons.sublime-build -O SCons.sublime-build
        echo "import os" > install.py
        echo "from mako.template import Template" >> install.py
        echo "with open(os.environ.get('HOME') + '/.config/sublime-text-'+os.environ.get('SUBLIME_TEXT') + '/Packages/User/SCons.sublime-build', 'w') as filehandler:" >> install.py
        echo "    filehandler.write(Template(filename='SCons.sublime-build').render(CONDA_DIR=os.environ.get('CONDA_DIR'), project_path='${project_path}'))" >> install.py
        python install.py
        rm install.py
        rm SCons.sublime-build
        if [[ "$REMOVE_MAKO" = "1" ]]; then
            conda remove mako -y
        fi
    fi
fi

if [[ "$ERROR" = "0" ]]; then
    echo "Developer configuration succeded."
fi

set +v
