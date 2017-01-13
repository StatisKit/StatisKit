#!/bin/sh

source activate ~/Desktop/miniconda2/bin/activate
if [[ -f environment.yml ]]; then
	ENVIRONMENT=`cat environment.yml | shyaml get-value name`
	conda env create -f environment.yml
	source activate $ENVIRONMENT
fi