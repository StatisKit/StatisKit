set -ve

python setup.py install --standard-lib --prefix=$PREFIX

mkdir -p $PREFIX/etc/conda/activate.d
mkdir -p $PREFIX/etc/conda/deactivate.d
touch $PREFIX/etc/conda/activate.d/scons_vars.sh
touch $PREFIX/etc/conda/deactivate.d/scons_vars.sh

cat > $PREFIX/etc/conda/activate.d/scons_vars.sh <<EOL
#!/bin/sh

export SCONSFLAGS="--site-dir=`python -c "import SCons; print(SCons.__path__[0])"`/site_scons"
EOL

cat > $PREFIX/etc/conda/deactivate.d/scons_vars.sh <<EOL
#!/bin/sh

unset SCONSFLAGS
unset SCONS_CONDAENV
EOL

if [[ "$PY3K" = "1" ]]; then
    2to3 -n -w $RECIPE_DIR/prefix.py
    2to3 -n -w $RECIPE_DIR/system.py
    2to3 -n -w $RECIPE_DIR/toolchain.py
    2to3 -n -w $RECIPE_DIR/conda.py
    2to3 -n -w $RECIPE_DIR/report.py
fi

mkdir -p $SP_DIR/SCons/site_scons
touch $SP_DIR/SCons/site_scons/__init__.py
touch $SP_DIR/SCons/site_scons/site_init.py
mkdir -p $SP_DIR/SCons/site_scons/site_tools
touch $SP_DIR/SCons/site_scons/site_tools/__init__.py
cp $RECIPE_DIR/prefix.py $SP_DIR/SCons/site_scons/site_tools/prefix.py
cp $RECIPE_DIR/system.py $SP_DIR/SCons/site_scons/site_tools/system.py
cp $RECIPE_DIR/toolchain.py $SP_DIR/SCons/site_scons/site_tools/toolchain.py
cp $RECIPE_DIR/conda.py $SP_DIR/SCons/site_scons/site_tools/conda.py
cp $RECIPE_DIR/report.py $SP_DIR/SCons/site_scons/site_tools/report.py

set +ve