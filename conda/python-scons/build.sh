$PYTHON setup.py install --standard-lib

mkdir -p $PREFIX/etc/conda/activate.d
mkdir -p $PREFIX/etc/conda/deactivate.d
touch $PREFIX/etc/conda/activate.d/scons_vars.sh
touch $PREFIX/etc/conda/deactivate.d/scons_vars.sh

cat > $PREFIX/etc/conda/activate.d/scons_vars.sh <<EOL
#!/bin/sh

export SCONSFLAGS="--sitedir=$CONDA_PREFIX/share/site_scons"
EOL

cat > $PREFIX/etc/conda/activate.d/scons_vars.sh <<EOL
#!/bin/sh

unset SCONSFLAGS
EOL

mkdir -p $PREFIX/share/site_scons
touch $PREFIX/share/site_scons/site_init.py
mkdir -p $PREFIX/share/site_scons/site_tools
