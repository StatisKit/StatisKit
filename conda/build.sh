set +x

REPOSITORY="PkgTk"
DEFAULT_BUILD_TARGETS="python-parse python-pkgtk"

ANACONDA_FLAGS="-c conda-forge "$ANACONDA_FLAGS
if [[ -z $ANACONDA_LABEL ]]; then
    ANACONDA_CHANNEL="statiskit"
else
    echo "Using anaconda label: "$ANACONDA_LABEL;
    ANACONDA_CHANNEL="statiskit/label/"$ANACONDA_LABEL;
    ANACONDA_FLAGS="-c statiskit "$ANACONDA_FLAGS;
fi

if [[ -z $BUILD_TARGETS ]]; then
    BUILD_TARGETS=$DEFAULT_BUILD_TARGETS;
else
    echo "Targets to build: "$BUILD_TARGETS;
fi

set -x

if [[ ! -f build.sh ]]; then
    if [[ -d "$REPOSITORY" ]]; then
        rm -rf $REPOSITORY;
    fi
    git clone https://github.com/$ANACONDA_CHANNEL/$REPOSITORY.git;
    if [ $? -ne 0 ]; then
        exit 1;
    fi
    cd PkgTk/conda;
fi

git clone https://gist.github.com/c491cb08d570beeba2c417826a50a9c3.git toolchain
if [ $? -ne 0 ]; then
    if [[ -d "$REPOSITORY" ]]; then
        rm -rf $REPOSITORY;
    fi
    exit 1;
fi
cd toolchain
source config.sh
if [ $? -ne 0 ]; then
    cd ..
    if [[ -d "$REPOSITORY" ]]; then
        rm -rf $REPOSITORY;
    fi
    rm -rf toolchain;
    exit 1;
fi
cd ..
rm -rf toolchain

for BUILD_TARGET in $BUILD_TARGETS; do
  conda build $BUILD_TARGET -c $ANACONDA_CHANNEL $ANACONDA_FLAGS
  if [ $? -ne 0 ]; then
    if [[ -d "$REPOSITORY" ]]; then
        rm -rf $REPOSITORY;
    fi
    exit 1;
  fi
done

if [[ -d "$REPOSITORY" ]]; then
    rm -rf $REPOSITORY;
fi