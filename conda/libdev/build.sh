source $RECIPE_DIR/pre-link.sh

mv $RECIPE_DIR/toolchains.py $SP_DIR/SCons/site_scons/site_tools/toolchains.py
mv $RECIPE_DIR/boost_python.py $SP_DIR/SCons/site_scons/site_tools/boost_python.py
