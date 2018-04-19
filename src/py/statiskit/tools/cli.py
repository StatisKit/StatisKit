## Copyright [2017] UMR MISTEA INRA, UMR LEPSE INRA, UMR AGAP CIRAD,     ##
##                  EPI Virtual Plants Inria                             ##
##                                                                       ##
## This file is part of the StatisKit project. More information can be   ##
## found at                                                              ##
##                                                                       ##
##     http://statiskit.rtfd.io                                          ##
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

import argparse
import os

from devops_tools import conda

from . import sublime_text

def main_build_system():

    parser = argparse.ArgumentParser()
    parser.add_argument('editor',
                        help = "Editor to configure",
                        choices = ["sublime_text"])
    args = parser.parse_args()

    if args.editor == "sublime_text":
        configs = sublime_text.config_paths()
        for config in configs:
            directory = os.path.join(config, 'Packages', 'StatisKit')
            if not os.path.exists(directory):
                os.makedirs(directory)
            with open(os.path.join(directory, 'StatisKit.sublime-build'), 'w') as filehandler:
                filehandler.write(sublime_text.BUILD_SYSTEM.replace('{{ prefix }}', conda.default_prefix()).replace('{{ environment }}', conda.current_environment()))
            with open(os.path.join(directory, 'StatisKit.py'), 'w') as filehandler:
                filehandler.write(sublime_text.BUILD_TARGET)