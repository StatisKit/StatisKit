#!/bin/sh

mngit init
#mngit github --remote=origin
mkdir doc
touch doc/index.rst
mkdir src
touch README.rst
git add doc README.rst
git commit -m 'Initialize the repository'
mngit authors
mngit version
mngit license --plugin=CeCILL-C
mngit rst
#mngit sphinx
mngit update
git add AUTHORS.rst LICENSE.rst
git commit -a --amend --no-edit
git push
