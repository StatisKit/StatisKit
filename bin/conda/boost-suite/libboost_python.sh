set -ve

python ${RECIPE_DIR}/move.py --src=${SRC_DIR}/Library/lib --dst=${PREFIX}/lib --include=boost_python

set +ve