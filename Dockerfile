FROM ubuntu:14.04

# Update the OS
RUN apt-get update

# Install useful tools
RUN apt-get install -y build-essential git wget

# Add user for future work
RUN useradd -ms /bin/bash conda-user

# select created user
USER conda-user

# Install miniconda
RUN wget https://repo.continuum.io/miniconda/Miniconda2-latest-Linux-x86_64.sh -O \ 
  $HOME/miniconda.sh
RUN bash $HOME/miniconda.sh -b -p $HOME/miniconda
RUN echo 'export PATH=$PATH:$HOME/miniconda/bin' >> $HOME/.bashrc 
RUN $HOME/miniconda/bin/conda config --set always_yes yes --set changeps1 no
RUN $HOME/miniconda/bin/conda update -q conda
RUN $HOME/miniconda/bin/conda info -a

# Install conda-build
RUN $HOME/miniconda/bin/conda install conda-build