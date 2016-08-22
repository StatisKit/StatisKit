FROM ubuntu:14.04

RUN sed -i 's/# \(.*multiverse$\)/\1/g' /etc/apt/sources.list

# Update the OS
RUN apt-get update

# Upgrade the OS
RUN apt-get -y upgrade

# Install useful tools
RUN apt-get install -y build-essential git wget firefox x11vnc xvfb

# Add user for future work
RUN useradd -ms /bin/bash conda-user

# select created user
USER conda-user

# Configure VNC
RUN mkdir $HOME/.vnc
RUN x11vnc -storepasswd 1234 $HOME/.vnc/passwd

# Install miniconda
RUN wget https://repo.continuum.io/miniconda/Miniconda2-latest-Linux-x86_64.sh -O \ 
  $HOME/miniconda.sh
RUN bash $HOME/miniconda.sh -b -p $HOME/miniconda
RUN rm $HOME/miniconda.sh
RUN echo 'export PATH=$PATH:$HOME/miniconda/bin' >> $HOME/.bashrc 
RUN $HOME/miniconda/bin/conda config --set always_yes yes --set changeps1 no
RUN $HOME/miniconda/bin/conda update -q conda
RUN $HOME/miniconda/bin/conda info -a

# Install conda-build
RUN $HOME/miniconda/bin/conda install conda-build==1.21.7

# Install IPython
RUN $HOME/miniconda/bin/conda install ipython

# Install Jupyter
RUN $HOME/miniconda/bin/conda install jupyter

# Install libraries and packages from Misc
## Clone the repository
RUN git clone https://github.com/Statiskit/Misc.git $HOME/Misc
RUN git -C $HOME/Misc pull

## Create a file for anaconda upload
RUN touch $HOME/upload.sh
RUN echo "set -e" >> $HOME/upload.sh
RUN echo "conda install anaconda-client" >> $HOME/upload.sh

## libboost recipe
RUN $HOME/miniconda/bin/conda build $HOME/Misc/libboost -c statiskit
RUN echo "anaconda upload \`conda build $HOME/Misc/libboost --output\` --user statiskit --force" >> $HOME/upload.sh

## python-scons recipe
RUN $HOME/miniconda/bin/conda build $HOME/Misc/python-scons -c statiskit
RUN echo "anaconda upload \`conda build $HOME/Misc/python-scons --output\` --user statiskit --force" >> $HOME/upload.sh

## python-parse recipe
RUN $HOME/miniconda/bin/conda build $HOME/Misc/python-parse -c statiskit
RUN echo "anaconda upload \`conda build $HOME/Misc/python-parse --output\` --user statiskit --force" >> $HOME/upload.sh

## Finalize file for anaconda upload
RUN echo "rm -rf $HOME/Misc" >> $HOME/upload.sh
RUN echo "conda remove anaconda-client" >> $HOME/upload.sh
RUN echo "conda clean --all" >> $HOME/upload.sh
RUN echo "rm $HOME/upload.sh" >> $HOME/upload.sh

WORKDIR /home/conda-user