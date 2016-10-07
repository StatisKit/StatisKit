set -xe

git clone https://github.com/StatisKit/Misc.git
cd Misc/conda

git clone https://gist.github.com/c491cb08d570beeba2c417826a50a9c3.git toolchain
cd toolchain
eval config.sh
cd ..

for CONDA_RECIPE in libboost python-scons; do
  conda build $CONDA_RECIPE -c statiskit &> /dev/null &
  pid=$! # Get PID of background command
  while kill -0 $pid; do
    echo -n "."
    sleep 60
  done
done
