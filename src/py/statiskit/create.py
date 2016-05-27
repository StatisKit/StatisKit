##################################################################################
#                                                                                #
# StatisKit: meta-repository providing general documentation and tools for the   #
# **StatisKit** Organization                                                     #
#                                                                                #
# Copyright (c) 2016 Pierre Fernique                                             #
#                                                                                #
# This software is distributed under the CeCILL-C license. You should have       #
# received a copy of the legalcode along with this work. If not, see             #
# <http://www.cecill.info/licences/Licence_CeCILL-C_V1-en.html>.                 #
#                                                                                #
# File authors: Pierre Fernique <pfernique@gmail.com> (10)                       #
#                                                                                #
##################################################################################

import os
from mako.template import Template
from statiskit.tools import list_input
import yaml
from distutils.util import strtobool

INDEX = Template(text=r"""\
|NAME|: |BRIEF|
${"###############"}

.. sidebar:: Summary

    :Version: |VERSION|
    :Status: |TRAVIS| |COVERALLS| |LANDSCAPE|
    :Authors: see `Authors`_ section
    :License: |LICENSENAME| (see `License`_ section)

|DETAILS|

Documentation
=============

.. toctree::
    :maxdepth: 2

    user/index
    developper/index
    maintener/index
    reference/index

Authors
=======

.. include:: ../AUTHORS.rst

License
=======

|NAME| is distributed under the |LICENSELINK|_.

.. |LICENSELINK| replace:: |LICENSENAME| license

.. _LICENSELINK : license.html

""")

README = Template(text=r"""\
|NAME|: |BRIEF|
${"###############"}

|DETAILS|

.. list-table::
    :stub-columns: 1

    * - Version
      - |VERSION|
    * - Status
      - |TRAVIS| |COVERALLS| |LANDSCAPE|
    * - Authors
      - see |AUTHORSFILE|_ file
    * - License
      - |LICENSENAME| (see |LICENSEFILE|_ file)

""")

GITIGNORE = r"""\
doc/_*
*.egg-info
*~
*.back
build
*.pyc
*.so
*.so
*.o
.coverage
"""

SETUP = r"""\
import os
from setuptools import setup, find_packages

packages = {"" : "src" + os.sep + "py"}
for package in find_packages("src" + os.sep + "py"):
    packages[package] = "src" + os.sep + "py"

try:
    from mngit.config import load_config
    config = load_config('.')
except:
    import os
    import yaml
    with open('.' + os.sep + '.mngit.yml', 'r') as filehandler:
        config = yaml.load(filehandler.read())

with open('README.rst', 'r') as filehandler:
    long_description = filehandler.read()

setup(packages = packages.keys(),
      package_dir = {"" : "src" + os.sep + "py"},
      name = config['about']['name'],
      version = config['about']['version'],
      author = config['about']['authors'],
      author_email = config['about']['email'],
      description = config['about']['brief'],
      long_description = long_description,
      license = config['license']['plugin'])
"""

SCONSTRUCT = ""

SCONSCRIPT = dict(cpp = "",
                  py = "")

INIT = r"""\
try:
    import pkg_resources
    pkg_resources.declare_namespace(__name__)
except ImportError:
    import pkgutil
    __path__ = pkgutil.extend_path(__path__, __name__)
"""

def overwrite(filename):
    if os.path.exists(filename):
        return strtobool(raw_input("Overwrite the '" + filename + "' file [y/n]: "))
    else:
        return True

def adapt_git(reponame):
    filenames = []

    filename = reponame + os.sep + 'README.rst'
    if overwrite(filename):
        with open(filename, 'w') as filehandler:
            filehandler.write(README.render(name = reponame))
        filenames.append(os.path.relpath(filename, reponame))

    filename = reponame + os.sep + '.travis.yml'
    if overwrite(filename):
        with open(filename, 'w') as filehandler:
            filehandler.write(yaml.dump(dict(after_success = 'coveralls'),
                default_flow_style=False))
        filenames.append(os.path.relpath(filename, reponame))

    filename = reponame + os.sep + '.gitignore'
    if overwrite(filename):
        with open(filename, 'w') as filehandler:
            filehandler.write(GITIGNORE)
        filenames.append(os.path.relpath(filename, reponame))
    return filenames

def create_doc(reponame):
    filenames = []
    dirname = reponame + os.sep + 'doc'
    if not os.path.exists(dirname):
        os.mkdir(dirname)
    filename = dirname + os.sep + 'index.rst'
    if overwrite(filename):
        with open(filename, 'w') as filehandler:
            filehandler.write(INDEX.render(name = reponame))
        filenames.append(os.path.relpath(filename, reponame))
    for subname in ['user', 'developper', 'maintener', 'reference']:
        subname = dirname + os.sep + subname
        if not os.path.exists(subname):
            os.mkdir(subname)
        filename = subname + os.sep + 'index.rst'
        if overwrite(filename):
            with open(filename, 'w') as filehandler:
                filehandler.write(subname.capitalize() + ' guide\n' + '#' * (len(subname) + 6) + '\n\n')
            filenames.append(os.path.relpath(filename, reponame))
    filename = dirname + os.sep + 'license.rst'
    if overwrite(filename):
        with open(filename, 'w') as filehandler:
            filehandler.write('.. include:: ../LICENSE.rst\n\n')
        filenames.append(os.path.relpath(filename, reponame))
    dirname = reponame + os.sep + 'src'
    if not os.path.exists(dirname):
        os.mkdir(dirname)
    return filenames

def create_py(reponame):
    filenames = []
    filename = reponame + os.sep + 'setup.py'
    if overwrite(filename):
        with open(filename, 'w') as filehandler:
            filehandler.write(SETUP)
        filenames.append(os.path.relpath(filename, reponame))
    srcname = reponame + os.sep + 'src' + os.sep + 'py'
    dirname = srcname + os.sep + reponame.lower().replace('_', '.').replace('-', '.').replace('.', os.sep)
    if not os.path.exists(dirname):
        os.makedirs(dirname)
    filename = dirname + os.sep + '__init__.py'
    if overwrite(filename):
        with open(filename, 'w'):
            pass
    filenames.append(os.path.relpath(filename, reponame))
    dirname = os.path.split(dirname)[0]
    while not dirname == srcname:
        filename = dirname + os.sep + '__init__.py'
        if overwrite(filename):
            with open(filename, 'w') as filehandler:
                filehandler.write(INIT)
            filenames.append(os.path.relpath(filename, reponame))
        dirname = os.path.split(dirname)[0]
    return filenames

def create_cpp(reponame):
    filenames = []
    filename = reponame + os.sep + 'SConstruct'
    if overwrite(filename):
        with open(filename, 'w') as filehandler:
            filehandler.write(SCONSTRUCT)
        filenames.append(os.path.relpath(filename, reponame))
    dirname = reponame + os.sep + 'src' + os.sep + 'cpp'
    if not os.path.exists(dirname):
        os.mkdir(dirname)
    filename = dirname + os.sep + 'SConscript'
    if overwrite(filename):
        with open(filename, 'w') as filehandler:
            filehandler.write(SCONSCRIPT['cpp'])
        filenames.append(os.path.relpath(filename, reponame))
    return filenames

def create_cpp_py(reponame):
    filenames = []
    filename = reponame + os.sep + 'src' + os.sep + 'py' + os.sep + 'SConscript'
    if overwrite(filename):
        with open(filename, 'w') as filehandler:
            filehandler.write(SCONSCRIPT['py'])
        filenames.append(os.path.relpath(filename, reponame))
    return filenames

def create(reponame, languages):

    if 'py' not in languages and os.path.exists(os.path.join(reponame, 'src', 'py')):
        languages.append('py')
    if 'cpp' not in languages and os.path.exists(os.path.join(reponame, 'src', 'cpp')):
        languages.append('cpp')

    filenames = []

    filenames.extend(adapt_git(reponame))

    filenames.extend(create_doc(reponame))

    if 'py' in languages:
        filenames.extend(create_py(reponame))

    if 'cpp' in languages:
        filenames.extend(create_cpp(reponame))

    if 'cpp' in languages and 'py' in languages:
        filenames.extend(create_cpp_py(reponame))

    return filenames
