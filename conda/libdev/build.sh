set -ve

source $RECIPE_DIR/post-link.sh

cp $RECIPE_DIR/cpp.py $SP_DIR/SCons/site_scons/site_tools/cpp.py

set +ve