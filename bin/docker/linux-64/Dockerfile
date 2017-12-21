ARG CONDA_VERSION=2
ARG UBUNTU_VERSION=14.04
FROM ubuntu:$UBUNTU_VERSION

ARG CONDA_VERSION

RUN apt-get update
RUN apt-get -y upgrade
RUN apt-get install vim wget curl bzip2 build-essential -y
RUN apt-get purge 
RUN apt-get clean

RUN useradd -m main --shell /bin/bash && echo "main:main" | chpasswd && adduser main sudo
USER main
WORKDIR /home/main

RUN curl "https://repo.continuum.io/miniconda/Miniconda"$CONDA_VERSION"-latest-Linux-x86_64.sh" -o miniconda.sh
RUN chmod a+rwx miniconda.sh
RUN ./miniconda.sh -b -p /home/main/miniconda
RUN rm miniconda.sh
env PATH /home/main/miniconda:/home/main/miniconda/bin:$PATH
env ARCH 64
RUN chmod -R a+rwx /home/main/miniconda
RUN conda config --set always_yes yes
RUN conda install git conda-build anaconda-client
RUN echo "source activate root" >> .bashrc

COPY build.sh /home/main/build.sh
COPY deploy.sh /home/main/deploy.sh
COPY install.sh /home/main/install.sh