# Build python-pkgtk recipe
conda build conda/python-pkgtk -c statiskit -c conda-forge
conda install python-pkgtk --use-local -c statiskit -c conda-forge
