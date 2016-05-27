import os
from mako.template import Template
from statiskit.tools import list_input

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
*.egg-info
*~
*.back
build-scons
*.pyc
*.so
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

def create(reponame):
    filenames = []
    dirname = reponame + os.sep + 'doc'
    if not os.path.exists(dirname):
        os.mkdir(dirname)
    filename = dirname + os.sep + 'index.rst'
    if not os.path.exists(filename) or list_input("Overwrite the '" + filename + "' file", ['y', 'n'], 'n') == 'y':
        with open(filename, 'w') as filehandler:
            filehandler.write(INDEX.render(name = reponame))
        filenames.append(os.path.relpath(filename, reponame))
    for subname in ['user', 'developper', 'maintener', 'reference']:
        subname = dirname + os.sep + subname
        if not os.path.exists(subname):
            os.mkdir(subname)
        filename = subname + os.sep + 'index.rst'
        if not os.path.exists(filename) or list_input("Overwrite the '" + filename + "' file", ['y', 'n'], 'n') == 'y':
            with open(filename, 'w') as filehandler:
                filehandler.write(subname.capitalize() + ' guide\n' + '#' * (len(subname) + 6) + '\n\n')
            filenames.append(os.path.relpath(filename, reponame))
    filename = dirname + os.sep + 'license.rst'
    if not os.path.exists(filename) or list_input("Overwrite '" + filename + "' file", ['y', 'n'], 'n') == 'y':
        with open(filename, 'w') as filehandler:
            filehandler.write('.. include:: ../LICENSE.rst\n\n')
        filenames.append(os.path.relpath(filename, reponame))
    dirname = reponame + os.sep + 'src'
    if not os.path.exists(dirname):
        os.mkdir(dirname)

    filename = reponame + os.sep + 'README.rst'
    if not os.path.exists(filename) or list_input("Overwrite the '" + filename + "' file", ['y', 'n'], 'n') == 'y':
        with open(filename, 'w') as filehandler:
            filehandler.write(README.render(name = reponame))
        filenames.append(os.path.relpath(filename, reponame))

    filename = reponame + os.sep + '.travis.yml'
    if not os.path.exists(filename) or list_input("Overwrite the '" + filename + "' file", ['y', 'n'], 'n') == 'y':
        with open(filename, 'w') as filehandler:
            filehandler.write(yaml.dump(dict(after_success = 'coveralls'),
                default_flow_style=False))
        filenames.append(os.path.relpath(filename, reponame))

    filename = reponame + os.sep + '.gitignore'
    if not os.path.exists(filename) or list_input("Overwrite the '" + filename + "' file", ['y', 'n'], 'n') == 'y':
        with open(filename, 'w') as filehandler:
            filehandler.write(GITIGNORE)
        filenames.append(os.path.relpath(filename, reponame))

    filename = reponame + os.sep + 'setup.py'
    if not os.path.exists(filename) and 'py' in args.languages or os.path.exists(filename) and list_input("Overwrite '" + filename + "' file", ['y', 'n'], 'n') == 'y':
        with open(filename, 'w') as filehandler:
            filehandler.write(SETUP)
        filenames.append(os.path.relpath(filename, reponame))
    if 'py' in args.languages:
        srcname = reponame + os.sep + 'src' + os.sep + 'py'
        dirname = srcname + os.sep + reponame.lower().replace('_', '.').replace('-', '.').replace('.', os.sep)
        if not os.path.exists(dirname):
            os.makedirs(dirname)
        filename = dirname + os.sep + '__init__.py'
        if not os.path.exists(filename) or list_input("Overwrite the '" + filename + "' file", ['y', 'n'], 'n') == 'y':
            with open(filename, 'w'):
                pass
        filenames.append(os.path.relpath(filename, reponame))
        dirname = os.path.split(dirname)[0]
        while not dirname == srcname:
            filename = dirname + os.sep + '__init__.py'
            if not os.path.exists(filename) or list_input("Overwrite the '" + filename + "' file", ['y', 'n'], 'n') == 'y':
                with open(filename, 'w') as filehandler:
                    filehandler.write(INIT)
                filenames.append(os.path.relpath(filename, reponame))
            dirname = os.path.split(dirname)[0]
    filename = reponame + os.sep + 'SConstruct'
    if not os.path.exists(filename) and 'cpp' in args.languages or os.path.exists(filename) and list_input("Overwrite '" + filename + "' file", ['y', 'n'], 'n') == 'y':
        with open(filename, 'w') as filehandler:
            filehandler.write(SCONSTRUCT)
        filenames.append(os.path.relpath(filename, reponame))
    dirname = reponame + os.sep + 'src' + os.sep + 'cpp'
    if not os.path.exists(dirname):
        os.mkdir(dirname)
    filename = dirname + os.sep + 'SConscript'
    if not os.path.exists(filename) and 'cpp' in args.languages or os.path.exists(filename) and list_input("Overwrite '" + filename + "' file", ['y', 'n'], 'n') == 'y':
        with open(filename, 'w') as filehandler:
            filehandler.write(SCONSCRIPT['cpp'])
        filenames.append(os.path.relpath(filename, reponame))
    filename = reponame + os.sep + 'src' + os.sep + 'py' + os.sep + 'SConscript'
    if not os.path.exists(filename) and 'cpp' in args.languages and 'py' in args.languages or os.path.exists(filename) and list_input("Overwrite '" + filename + "' file", ['y', 'n'], 'n') == 'y':
        with open(filename, 'w') as filehandler:
            filehandler.write(SCONSCRIPT['py'])
        filenames.append(os.path.relpath(filename, reponame))
    return filenames
