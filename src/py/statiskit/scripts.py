import os
from argparse import ArgumentParser, RawTextHelpFormatter
import shutil
from github import Github
from getpass import getpass
from git import Repo
import os
from mako.template import Template
from mngit.scripts import mngit
import subprocess
import yaml

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

def list_input(msg, items, default):
    answer = raw_input(msg + " [" + '/'.join(items)+ "]: ")
    while answer and not answer in items:
        answer = raw_input(msg + " [" + '/'.join(items)+ "]: ")
    if not answer:
        answer = default
    return answer

def create_script(args):
    username = raw_input("Username for 'https://github.com': ")
    password = getpass("Password for 'https://" + username + "@github.com': ")
    account = Github(username,
                     password)
    organization = account.get_organization('StatisKit')
    name = raw_input("Enter a repository name: ")
    try:
        remote = organization.create_repo(name)
    except:
        remote = organization.get_repo(name)
    if remote.description:
        brief = raw_input("Overwrite the brief description: ")
        if brief:
            remote.edit(name, description = brief)
        else:
            brief = remote.description
    else:
        brief = raw_input("Enter a brief description: ")
        # TODO character limits
        remote.edit(name, description = brief)

    if os.path.exists(name):
        raise ValueError()

    local = Repo.clone_from(remote.html_url, name)

    dirname = name + os.sep + 'doc'
    if not os.path.exists(dirname):
        os.mkdir(dirname)
        local.index.add([os.path.relpath(dirname, name)])
    filename = dirname + os.sep + 'index.rst'
    if not os.path.exists(filename) or list_input("Overwrite the '" + filename + "' file", ['y', 'n'], 'n') == 'y':
        with open(filename, 'w') as filehandler:
            filehandler.write(INDEX.render(name = name))
        local.index.add([os.path.relpath(filename, name)])
    for subname in ['user', 'developper', 'maintener', 'reference']:
        subname = dirname + os.sep + subname
        if not os.path.exists(subname):
            os.mkdir(subname)
            local.index.add([os.path.relpath(subname, name)])
        filename = subname + os.sep + 'index.rst'
        if not os.path.exists(filename) or list_input("Overwrite the '" + filename + "' file", ['y', 'n'], 'n') == 'y':
            with open(filename, 'w') as filehandler:
                filehandler.write(subname.capitalize() + ' guide\n' + '#' * (len(subname) + 6) + '\n\n')
            local.index.add([os.path.relpath(filename, name)])
    filename = dirname + os.sep + 'license.rst'
    if not os.path.exists(filename) or list_input("Overwrite '" + filename + "' file", ['y', 'n'], 'n') == 'y':
        with open(filename, 'w') as filehandler:
            filehandler.write('.. include:: ../LICENSE.rst\n\n')
        local.index.add([os.path.relpath(filename, name)])
    dirname = name + os.sep + 'src'
    if not os.path.exists(dirname):
        os.mkdir(dirname)
    #for language in args.languages:
    #    subdirname = dirname + os.sep + language
    #    if not os.path.exists(subdirname):
    #        os.mkdir(subdirname)
    #    filename = subdirname + os.sep + '.gitignore'
    #    if not os.path.exists(filename):
    #        with open(filename, 'w') :
    #            pass
    #        local.index.add([os.path.relpath(filename, name)])

    filename = name + os.sep + 'README.rst'
    if not os.path.exists(filename) or list_input("Overwrite the '" + filename + "' file", ['y', 'n'], 'n') == 'y':
        with open(filename, 'w') as filehandler:
            filehandler.write(README.render(name = name))
        local.index.add([os.path.relpath(filename, name)])

    filename = name + os.sep + '.travis.yml'
    if not os.path.exists(filename) or list_input("Overwrite the '" + filename + "' file", ['y', 'n'], 'n') == 'y':
        with open(filename, 'w') as filehandler:
            filehandler.write(yaml.dump(dict(after_success = 'coveralls'),
                default_flow_style=False))
        local.index.add([os.path.relpath(filename, name)])

    filename = name + os.sep + '.gitignore'
    if not os.path.exists(filename) or list_input("Overwrite the '" + filename + "' file", ['y', 'n'], 'n') == 'y':
        with open(filename, 'w') as filehandler:
            filehandler.write(GITIGNORE)
        local.index.add([os.path.relpath(filename, name)])

    filename = name + os.sep + 'setup.py'
    if not os.path.exists(filename) and 'py' in args.languages or os.path.exists(filename) and list_input("Overwrite '" + filename + "' file", ['y', 'n'], 'n') == 'y':
        with open(filename, 'w') as filehandler:
            filehandler.write(SETUP)
        local.index.add([os.path.relpath(filename, name)])
    if 'py' in args.languages:
        srcname = name + os.sep + 'src' + os.sep + 'py'
        dirname = srcname + os.sep + name.lower().replace('_', '.').replace('-', '.').replace('.', os.sep)
        if not os.path.exists(dirname):
            os.makedirs(dirname)
        filename = dirname + os.sep + '__init__.py'
        if not os.path.exists(filename) or list_input("Overwrite the '" + filename + "' file", ['y', 'n'], 'n') == 'y':
            with open(filename, 'w'):
                pass
        local.index.add([os.path.relpath(filename, name)])
        dirname = os.path.split(dirname)[0]
        while not dirname == srcname:
            filename = dirname + os.sep + '__init__.py'
            if not os.path.exists(filename) or list_input("Overwrite the '" + filename + "' file", ['y', 'n'], 'n') == 'y':
                with open(filename, 'w') as filehandler:
                    filehandler.write(INIT)
                local.index.add([os.path.relpath(filename, name)])
            dirname = os.path.split(dirname)[0]
    filename = name + os.sep + 'SConstruct'
    if not os.path.exists(filename) and 'cpp' in args.languages or os.path.exists(filename) and list_input("Overwrite '" + filename + "' file", ['y', 'n'], 'n') == 'y':
        with open(filename, 'w') as filehandler:
            filehandler.write(SCONSTRUCT)
        local.index.add([os.path.relpath(filename, name)])
    dirname = name + os.sep + 'src' + os.sep + 'cpp'
    if not os.path.exists(dirname):
        os.mkdir(dirname)
    filename = dirname + os.sep + 'SConscript'
    if not os.path.exists(filename) and 'cpp' in args.languages or os.path.exists(filename) and list_input("Overwrite '" + filename + "' file", ['y', 'n'], 'n') == 'y':
        with open(filename, 'w') as filehandler:
            filehandler.write(SCONSCRIPT['cpp'])
        local.index.add([os.path.relpath(filename, name)])
    filename = name + os.sep + 'src' + os.sep + 'py' + os.sep + 'SConscript'
    if not os.path.exists(filename) and 'cpp' in args.languages and 'py' in args.languages or os.path.exists(filename) and list_input("Overwrite '" + filename + "' file", ['y', 'n'], 'n') == 'y':
        with open(filename, 'w') as filehandler:
            filehandler.write(SCONSCRIPT['py'])
        local.index.add([os.path.relpath(filename, name)])

    authors = ', '.join(member.name for member in organization.get_members() if member.name)
    mngit(['init', '--root', name, '--name', name, '--brief', brief, '--authors', authors, '--email', organization.email])
    mngit(['authors', '--root', name])
    mngit(['license', '--root', name, '--plugin', 'CeCILL-C'])
    mngit(['version', '--root', name])
    mngit(['rst', '--root', name, '--target', 'README.rst', 'doc/index.rst'])
    mngit(['travis', '--root', name, '--account', 'StatisKit', '--project', name])
    mngit(['coveralls', '--root', name, '--account', 'StatisKit', '--project', name])
    mngit(['landscape', '--root', name, '--account', 'StatisKit', '--project', name])
    mngit(['readthedocs', '--root', name, '--project', name])

    local.index.add(['.mngit.yml'])

    message = raw_input("Enter a brief commit message: ")
    local.index.commit(message)

    mngit(['update', '--root', name])
    local.index.add([entry[0] for entry in local.index.entries] + ['AUTHORS.rst', 'LICENSE.rst'])
    local.git.commit(['--amend', '--no-edit'])

    subprocess.call(['git', 'push', 'https://' + username + ':' + password + '@' + remote.html_url.lstrip('https://')], cwd=name)

    shutil.rmtree(name)


def statiskit(args=None):
    parser = ArgumentParser(description='Repository manager for StatisKit organization',
            formatter_class=RawTextHelpFormatter)

    subparsers = parser.add_subparsers(title="These are the StatiKit commands used in various situations")

    subparser = subparsers.add_parser('create', help=create_script.__doc__)
    subparser.add_argument('--languages', type=str,
            nargs = '*',
            choices = ['cpp', 'py'],
            help="Source code languages")
    subparser.set_defaults(func = create_script)

    if args:
        args = parser.parse_args(args)
    else:
        args = parser.parse_args()

    args.func(args)
