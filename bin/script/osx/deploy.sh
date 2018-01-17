set -ve

for filename in $(find ${CONDA_PREFIX}/conda-bld/ -name '*.tar.bz2')
do
    anaconda upload ${filename} -u statiskit --label osx-release
done

set +ve
