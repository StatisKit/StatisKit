set -ve

export SITE_SCONS=`python -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())"`
export SITE_SCONS=$SITE_SCONS/scons_tools
if [[ "$SCONSFLAGS" = "" ]]; then
    export SCONSFLAGS=--site-dir=$SITE_SCONS
else
    export SCONSFLAGS=$SCONSFLAGS --site-dir=$SITE_SCONS
fi

set +ve