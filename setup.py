##################################################################################
#                                                                                #
# PkgTk: Tool kit for Python packages                                            #
#                                                                                #
# Homepage: pkg.readthedocs.io                                                 #
#                                                                                #
# Copyright (c) 2016 Pierre Fernique                                             #
#                                                                                #
# This software is distributed under the CeCILL-C license. You should have       #
# received a copy of the legalcode along with this work. If not, see             #
# <http://www.cecill.info/licences/Licence_CeCILL-C_V1-en.html>.                 #
#                                                                                #
# File authors: Pierre Fernique <pfernique@gmail.com> (13)                       #
#                                                                                #
##################################################################################

import os
from setuptools import setup, find_packages

packages = {"" : "src" + os.sep + "py"}
for package in find_packages("src" + os.sep + "py"):
    packages[package] = "src" + os.sep + "py"

try:
  from pkg.metadata import load_metadata
  metadata = load_metadata('.')
except:
  class MetaData(object):
    name = 'PkgTk'
    version = None
    authors = ''
    email = ''
    description = ''
    long_description = ''
    license = None
  metadata = MetaData()


setup(packages = packages.keys(),
      package_dir = {"" : "src" + os.sep + "py"},
      name = metadata.name,
      version = metadata.version,
      author = metadata.authors,
      author_email = metadata.email,
      description = metadata.description,
      long_description = metadata.long_description,
      license = metadata.license,
      entry_points = {'pkg.load_authors': ['commit = pkg.load_authors_commit:load_authors'],
                      'console_scripts': ['pkg = pkg.scripts:pkg'],
                      'pkg.load_about': ['github = pkg.load_about_github:load_about'],
                      'pkg.load_license': ['CeCILL-C = pkg.load_license_cecillc:load_license',
                                             'CeCILL = pkg.load_license_cecill:load_license']},
      zip_safe = False)

del metadata