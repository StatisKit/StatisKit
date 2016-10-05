set -xe

git clone https://github.com/StatisKit/Misc.git
cd Misc/conda

conda install python-pkgtk -c statiskit -c conda-forge
export TOOLCHAIN=`pkgtk toolchain`

for CONDA_RECIPE in libboost python-scons; do
  conda build $CONDA_RECIPE -c statiskit &> /dev/null
done
