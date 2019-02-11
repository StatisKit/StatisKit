ARG CONDA_VERSION=3
FROM statiskit/linux-64:latest-py${CONDA_VERSION}k

ARG CONDA_VERSION
RUN bash -c "eval $CONDA_ACTIVATE && conda create -n statiskit-toolchain statiskit-toolchain -c statiskit/label/statiskit-linux_x86_64-release -c statiskit -c defaults --override-channels"
RUN echo "conda activate statiskit-toolchain" >> ${HOME}/.bashrc