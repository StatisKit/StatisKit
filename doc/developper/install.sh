set -v

wget http://statiskit.readthedocs.io/en/latest/_downloads/install.sh -O pre-install.sh
source pre-install.sh
rm pre-install.sh

conda install conda-build
if [[ $? = 0 ]]; then
    conda update conda-build
fi
if [[ -d $HOME/.config/sublime-text-3 ]]; then
    export SUBLIME_TEXT=3
elif [[ -d $HOME/.config/sublime-text-2 ]]; then
    export SUBLIME_TEXT=2
fi
if [[ ! "$SUBLIME_TEXT"="" ]]; then
    conda update mako -c conda-forge
    wget http://statiskit.readthedocs.io/en/latest/developer/SCons.sublime-build -O SCons.sublime-build
    cat > install.py << EOL

import os
from mako.template import Template

with open(os.environ.get('HOME') + '/.config/sublime-text-'+os.environ.get('SUBLIME_TEXT') + '/Packages/User/SCons.sublime-build', 'w') as filehandler:
    filehandler.write(Template(filename = "SCons.sublime-build").render(CONDA_DIR = os.environ.get('CONDA_DIR')))
EOL
    python install.py
    rm install.py
    conda remove mako

fi

set +v