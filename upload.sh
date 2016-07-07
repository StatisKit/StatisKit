for i in $(ls -d */); do
	conda build ${i%%/};
fi
anaconda login
for i in $(ls -d */); do
    CONDA_FILE=`conda build ${i%%/} --output`;
    anaconda upload --user StatisKit ${CONDA_FILE%%};
fi