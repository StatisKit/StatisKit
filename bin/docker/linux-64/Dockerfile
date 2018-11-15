ARG CONDA_VERSION=3
ARG UBUNTU_VERSION=18.04
ARG USER_LOGIN=admin
ARG USER_PASSWORD=admin
ARG CONDA_PREFIX=miniconda
FROM ubuntu:${UBUNTU_VERSION}

ARG CONDA_VERSION
ARG USER_LOGIN
ARG USER_PASSWORD
ARG CONDA_PREFIX

RUN apt-get update
RUN apt-get -y upgrade
RUN apt-get install vim wget curl bzip2 git python python-six -y
RUN apt-get purge 
RUN apt-get clean

RUN useradd -m ${USER_LOGIN} --shell /bin/bash && echo "${USER_LOGIN}:${USER_PASSWORD}" | chpasswd && adduser ${USER_LOGIN} sudo
USER ${USER_LOGIN}
WORKDIR /home/${USER_LOGIN}

RUN git clone https://github.com/StatisKit/travis-ci.git travis-ci --depth=1
RUN cd travis-ci && bash install.sh 
RUN rm -rf travis-ci

env ARCH x86_64