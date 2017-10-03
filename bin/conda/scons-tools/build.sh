set -ve

mkdir -p $PREFIX/etc/conda/activate.d
cp $RECIPE_DIR/activate.sh $PREFIX/etc/conda/activate.d/scons_tools_vars.sh

mkdir -p $PREFIX/etc/conda/deactivate.d
cp $RECIPE_DIR/deactivate.sh $PREFIX/etc/conda/deactivate.d/scons_tools_vars.sh

export TGT_DIR=scons_tools
mkdir $SP_DIR/$TGT_DIR
touch $SP_DIR/$TGT_DIR/__init__.py
touch $SP_DIR/$TGT_DIR/site_init.py
export TGT_DIR=$TGT_DIR/site_tools
mkdir $SP_DIR/$TGT_DIR
touch $SP_DIR/$TGT_DIR/__init__.py

for SCONS_TOOL in `ls *.py`; do
    if [[ "$PY3K" = "1" ]]; then
        2to3 -n -w $SCONS_TOOL
    fi
    cp $SCONS_TOOL $SP_DIR/$TGT_DIR/$SCONS_TOOL
done

mkdir $SP_DIR/scons_tools/site_autowig
touch $SP_DIR/scons_tools/site_autowig/__init__.py
mkdir -p $SP_DIR/scons_tools/site_autowig/ASG
mkdir -p $SP_DIR/scons_tools/site_autowig/parser
touch $SP_DIR/scons_tools/site_autowig/parser/__init__.py
mkdir -p $SP_DIR/scons_tools/site_autowig/controller
touch $SP_DIR/scons_tools/site_autowig/controller/__init__.py
mkdir -p $SP_DIR/scons_tools/site_autowig/generator
touch $SP_DIR/scons_tools/site_autowig/generator/__init__.py

set +ve