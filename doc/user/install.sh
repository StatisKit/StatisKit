set -ev

if [[ "$CONDA_PREFIX" = "" ]]; then
    CONDA_PREFIX='$HOME/.conda'
fi
cd $CONDA_PREFIX
if [[ ! "$CONDA_VERSION" = "" ]]; then
    CONDA_VERSION=2
fi

if [[ ! -d CONDA_PREFIX ]]; then

    case "$(uname -s)" in
        Darwin)
            curl https://repo.continuum.io/miniconda/Miniconda$CONDA_VERSION-latest-MacOSX-x86_64.sh -o miniconda.sh
            ;;
        Linux)
            wget https://repo.continuum.io/miniconda/Miniconda$CONDA_VERSION-latest-Linux-x86_64.sh -O miniconda.sh
            ;;
        *)
            exit 1 
            ;;
    esac

    bash miniconda.sh -b -p $CONDA_PREFIX
    rm miniconda.sh
fi

export PATH=$CONDA_PREFIX/bin:$PATH

if [[ "$CONDA_ALWAYS_YES" = "" ]]; then
  CONDA_ALWAYS_YES=no
fi
if [[ "$CONDA_CHANGE_PS1" = "" ]]; then
  CONDA_CHANGE_PS1=yes
fi
conda config --set always_yes $CONDA_ALWAYS_YES
conda config --set changeps1 $CONDA_CHANGE_PS1
conda update -q conda

# if [[ -d $HOME/.config/sublime-text-3/Packages/SublimeREPL ]]; then
#     mkdir -p $HOME/.config/sublime-text-3/Packages/StatisKit
# fi

set +ev