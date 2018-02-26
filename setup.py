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

import six
import os
from setuptools import setup, find_packages

packages = {"" : "src" + os.sep + "py"}
for package in find_packages("src" + os.sep + "py"):
    packages[package] = "src" + os.sep + "py"

with open('README.rst', 'r') as filehandler:
    long_description = filehandler.read()

setup(packages = packages.keys(),
      package_dir = {"" : "src" + os.sep + "py"},
      name = 'statiskit-tools',
      version = '1.0.0',
      author = 'Pierre Fernique',
      author_email = 'pfernique@gmail.com',
      description = 'Tools for unifying software development and operation with the StatisKit organization',
      long_description = '',
      license = 'Apache License 2.0',
      package_data = {package: [ "*.so", "*.dll"] for package in packages},
      entry_points = {},
        zip_safe = True
    )