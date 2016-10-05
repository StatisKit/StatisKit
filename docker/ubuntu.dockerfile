FROM ubuntu:14.04

# Update the OS
RUN apt-get update

# Upgrade the OS
RUN apt-get -y upgrade

# Install useful tools
RUN apt-get install -y vim build-essential git wget curl
# firefox
RUN apt-get autoremove

# Add user for future work
RUN useradd -m main --shell /bin/bash && echo "main:main" | chpasswd && adduser main sudo

# select created user
USER main

# Install miniconda
RUN wget https://repo.continuum.io/miniconda/Miniconda2-latest-Linux-x86_64.sh \
         -O $HOME/miniconda.sh
RUN bash $HOME/miniconda.sh -b -p $HOME/miniconda
RUN rm $HOME/miniconda.sh
ENV PATH /home/main/miniconda/bin:$PATH
RUN conda config --set always_yes yes --set changeps1 no
RUN conda update -q conda
RUN conda info -a

# Install conda-build
RUN conda install conda-build

WORKDIR /home/main
