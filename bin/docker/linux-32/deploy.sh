set -ve

for filename in ${CONDA_PREFIX}/conda-bld/linux-${ARCH}/*.tar.bz2
do
    anaconda upload ${filename} -u statiskit --label linux-${ARCH}_release
done

set +ve
