set -ve

python ${RECIPE_DIR}/move.py --src=${SRC_DIR}/Library/include --dst=${PREFIX}/include

set +ve