set +v

if [[ "$OS_NAME" = "Linux" ]]; then
    if [[ -d "$HOME/.config/sublime-text-3" ]]; then
        export SUBLIME_TEXT=3
    elif [[ -d "$HOME/.config/sublime-text-2" ]]; then
        export SUBLIME_TEXT=2
    fi
    export SUBLIME_TEXT=~/.config/sublime-text-$SUBLIME_TEXT/Packages/User
else
    if [[ -d "$HOME/.config/sublime-text-3" ]]; then
        export SUBLIME_TEXT=3
    elif [[ -d "$HOME/.config/sublime-text-2" ]]; then
        export SUBLIME_TEXT=2
    fi
    export SUBLIME_TEXT=~/Library/Application\ Support/Sublime\ Text\ $SUBLIME_TEXT/Packages/User
fi
if [[ ! "$SUBLIME_TEXT" = "" ]]; then
    python -c "import mako" >/dev/null 2>/dev/null
    if [[ "$?" = "0" ]]; then
        export REMOVE_MAKO=0
    else
        export REMOVE_MAKO=1
        conda install mako -c conda-forge -y
    fi        
    if [[ ! "$?" = "0" ]]; then
        wget https://raw.githubusercontent.com/StatisKit/StatisKit/master/doc/developper/SCons.sublime-build -O SCons.sublime-build
        echo "import os" > install.py
        echo "from mako.template import Template" >> install.py
        echo "with open(os.environ.get('SUBLIME_TEXT') + '/SCons.sublime-build', 'w') as filehandler:" >> install.py
        echo "    filehandler.write(Template(filename='SCons.sublime-build').render(CONDA_DIR=os.environ.get('CONDA_DIR'), project_path='${project_path}'))" >> install.py
        python install.py
        if [[ ! "$?" = "0" ]]; then
            echo 'Sublime Text '$SUBLIME_TEXT' configuration failed.'
        fi
        rm install.py
        rm SCons.sublime-build
    fi
    if [[ "$REMOVE_MAKO" = "1" ]]; then
        conda remove mako -y
    fi
fi
source activate statiskit-dev
git config --system core.editor "subl -n -w"
source deactivate

set +v