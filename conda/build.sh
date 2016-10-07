set -e
set +x

[[ -z $BUILD_TARGETS ]] && BUILD_TARGETS="libboost python-scons" || echo "Targets to build: "$BUILD_TARGETS

set -x

git clone https://github.com/StatisKit/Misc.git
cd Misc/conda

git clone https://gist.github.com/c491cb08d570beeba2c417826a50a9c3.git toolchain
cd toolchain
eval config.sh
cd ..
rm -rf toolchain

for BUILD_TARGET in $BUILD_TARGETS; do
  conda build $BUILD_TARGET -c statiskit -c conda-forge &> /dev/null &
  pid=$! # Get PID of background command
  while kill -0 $pid; do
    echo -n "."
    sleep 60
  done
done
