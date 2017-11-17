## Copyright [2017-2018] UMR MISTEA INRA, UMR LEPSE INRA,                ##
##                       UMR AGAP CIRAD, EPI Virtual Plants Inria        ##
## Copyright [2015-2016] UMR AGAP CIRAD, EPI Virtual Plants Inria        ##
##                                                                       ##
## This file is part of the AutoWIG project. More information can be     ##
## found at                                                              ##
##                                                                       ##
##     http://autowig.rtfd.io                                            ##
##                                                                       ##
## The Apache Software Foundation (ASF) licenses this file to you under  ##
## the Apache License, Version 2.0 (the "License"); you may not use this ##
## file except in compliance with the License. You should have received  ##
## a copy of the Apache License, Version 2.0 along with this file; see   ##
## the file LICENSE. If not, you may obtain a copy of the License at     ##
##                                                                       ##
##     http://www.apache.org/licenses/LICENSE-2.0                        ##
##                                                                       ##
## Unless required by applicable law or agreed to in writing, software   ##
## distributed under the License is distributed on an "AS IS" BASIS,     ##
## WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or       ##
## mplied. See the License for the specific language governing           ##
## permissions and limitations under the License.                        ##

set -ve

mkdir -p $PREFIX/etc/conda/activate.d
cp $RECIPE_DIR/activate.sh $PREFIX/etc/conda/activate.d/scons_tools_vars.sh

mkdir -p $PREFIX/etc/conda/deactivate.d
cp $RECIPE_DIR/deactivate.sh $PREFIX/etc/conda/deactivate.d/scons_tools_vars.sh

export TGT_DIR=scons_tools
mkdir $SP_DIR/$TGT_DIR
touch $SP_DIR/$TGT_DIR/__init__.py
touch $SP_DIR/$TGT_DIR/site_init.py
export TGT_DIR=$TGT_DIR/site_tools
mkdir $SP_DIR/$TGT_DIR
touch $SP_DIR/$TGT_DIR/__init__.py

for SCONS_TOOL in `ls *.py`; do
    if [[ "$PY3K" = "1" ]]; then
        2to3 -n -w $SCONS_TOOL
    fi
    cp $SCONS_TOOL $SP_DIR/$TGT_DIR/$SCONS_TOOL
done

mkdir $SP_DIR/scons_tools/site_autowig
touch $SP_DIR/scons_tools/site_autowig/__init__.py
mkdir -p $SP_DIR/scons_tools/site_autowig/ASG
mkdir -p $SP_DIR/scons_tools/site_autowig/parser
touch $SP_DIR/scons_tools/site_autowig/parser/__init__.py
mkdir -p $SP_DIR/scons_tools/site_autowig/controller
touch $SP_DIR/scons_tools/site_autowig/controller/__init__.py
mkdir -p $SP_DIR/scons_tools/site_autowig/generator
touch $SP_DIR/scons_tools/site_autowig/generator/__init__.py

set +ve