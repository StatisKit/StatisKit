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

for i in $(ls -R -d ./*/*-[0-9]*.svg); do
    j=${i/svg/png}
    inkscape ${i} --export-png=${j} --export-area-drawing
done

sources=`ls -r -R -d ./branch/branch-[0-9]*.png`
target=./branch/branch.gif
convert -dispose previous -delay 100 ${sources} ${target}
convert -reverse ${target} ${target}

sources=`ls -r -R -d ./commit/commit-[0-9]*.png`
target=./commit/commit.gif
convert -dispose previous -delay 100 ${sources} ${target}
convert -reverse ${target} ${target}

sources=`ls -r -R -d ./upload/upload-[0-9]*.png`
target=./upload/upload.gif
convert -dispose previous -delay 100 ${sources} ${target}
convert -reverse ${target} ${target}

sources=`ls -r -R -d ./submit/prepare-[0-9]*.png`
target=./submit/prepare.gif
convert -dispose previous -delay 100 ${sources} ${target}
convert -reverse ${target} ${target}

sources=`ls -r -R -d ./submit/propose-[0-9]*.png`
target=./submit/propose.gif
convert -dispose previous -delay 100 ${sources} ${target}
convert -reverse ${target} ${target}

sources=`ls -r -R -d ./submit/integrate-[0-9]*.png`
target=./submit/integrate.gif
convert -dispose previous -delay 100 ${sources} ${target}
convert -reverse ${target} ${target}
