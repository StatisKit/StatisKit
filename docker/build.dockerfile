FROM statiskit/ubuntu

# Build libraries and packages from Misc
RUN git clone https://github.com/Statiskit/Misc.git $HOME/Misc
RUN cd $HOME/Misc/conda && bash build.sh
RUN conda env remove -n _build || echo "No _build environment"
RUN conda env remove -n _test || echo "No _test environment"
RUN conda clean --all -y

WORKDIR /home/main
