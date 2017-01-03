set -e

if [[ ! "$CONDA_PREFIX" = "" ]]; then
    cd $CONDA_PREFIX
else
    CONDA_PREFIX=`pwd`
fi
if [[ ! "$CONDA_VERSION" = "" ]]; then
    CONDA_VERSION=2
fi
wget https://repo.continuum.io/miniconda/Miniconda$CONDA_VERSION-latest-Linux-x86_64.sh -O miniconda.sh
bash miniconda.sh -b -p $CONDA_PREFIX/miniconda$CONDA_VERSION
if [[ "$CONDA_REMOVE" = "yes" ]]; then
    rm miniconda.sh
fi
if [[ "$PRINT_PATH" = "" ]]; then
    PRINT_PATH="yes"
fi
export PATH=$CONDA_PREFIX/miniconda/bin:$PATH
if [[ "$CONDA_ALWAYS_YES" = "" ]]; then
  CONDA_ALWAYS_YES=no
fi
if [[ "$CONDA_CHANGE_PS1" = "" ]]; then
  CONDA_CHANGE_PS1=yes
fi
conda config --set always_yes $CONDA_ALWAYS_YES
conda config --set changeps1 $CONDA_CHANGE_PS1
if [[ ! "$CONDA_BUILD_ROOT_DIR" = "" ]]; then
  echo "conda-build:" >> $HOME/.condarc;
  echo "  root-dir: " $CONDA_BUILD_ROOT_DIR >> $HOME/.condarc;
fi
conda update -q conda
conda info -a
conda install conda-build
conda install anaconda-client
rm install.sh