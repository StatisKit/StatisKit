#!/bin/bash

cd $PREFIX
mkdir -p ./etc/conda/activate.d
cd ./etc/conda/activate.d/
touch env_vars.sh

case "$OSTYPE" in

    linux*)
        echo "TOOLCHAIN=\`gcc -dumpversion\`" >> env_vars.sh
        ;;

    darwin*)
        echo "TOOLCHAIN=\`clang -dumpversion\`" >> env_vars.sh
        ;;

esac

echo "TOOLCHAIN=\${TOOLCHAIN%.*}" >> env_vars.sh
echo "TOOLCHAIN=\`echo \"\$TOOLCHAIN\" | tr -d .\`" >> env_vars.sh

case "$OSTYPE" in

    linux*)
        echo "TOOLCHAIN="gcc"\$TOOLCHAIN" >> env_vars.sh
        ;;

    darwin*)
        echo "TOOLCHAIN="clang"\$TOOLCHAIN" >> env_vars.sh
        ;;

esac

echo "export TOOLCHAIN=\$TOOLCHAIN" >> env_vars.sh

cd $PREFIX
mkdir -p ./etc/conda/deactivate.d
cd ./etc/conda/deactivate.d/
touch env_vars.sh
echo "unset TOOLCHAIN" >> env_vars.sh