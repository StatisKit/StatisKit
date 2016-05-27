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
# File authors: Pierre Fernique <pfernique@gmail.com> (9)                        #
#                                                                                #
##################################################################################

import os
from argparse import ArgumentParser, RawTextHelpFormatter
import shutil
from github import Github
from getpass import getpass
from git import Repo
from mngit.scripts import mngit
import subprocess

from statiskit.create import create

def create_script(args):
    username = raw_input("Username for 'https://github.com': ")
    password = getpass("Password for 'https://" + username + "@github.com': ")
    account = Github(username,
                     password)
    organization = account.get_organization('StatisKit')
    name = raw_input("Enter a repository name: ")
    try:
        remote = organization.create_repo(name)
    except Exception:
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

    filenames = create(name, args.languages)
    local.index.add(filenames)

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
    local.index.add(filenames + ['AUTHORS.rst', 'LICENSE.rst'])
    local.git.commit(['--amend', '--no-edit'])

    subprocess.call(['git', 'push', 'https://' + username + ':' + password + '@' + remote.html_url.lstrip('https://')], cwd=name)

    shutil.rmtree(name)

def clone_script(args):
    username = raw_input("Username for 'https://github.com': ")
    password = getpass("Password for 'https://" + username + "@github.com': ")
    account = Github(username,
                     password)
    organization = account.get_organization('StatisKit')
    name = raw_input("Enter a repository name: ")
    upstream = organization.get_repo(name)

    user = account.get_user()
    origin = None
    for remote in user.get_repos():
        if remote.parent == upstream:
            origin = remote
            break
    if origin is None:
        origin = user.create_fork(upstream)

    if os.path.exists(name):
        raise ValueError()

    if args.url == 'ssh':
        local = Repo.clone_from(origin.ssh_url, name)
        local.create_remote('upstream', upstream.ssh_url)
    elif args.url == 'html':
        local = Repo.clone_from(origin.html_url, name)
        local.create_remote('upstream', upstream.html_url)

    mngit(['update', '--root', name])

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

    subparser = subparsers.add_parser('clone', help=clone_script.__doc__)
    subparser.add_argument('--url', type=str,
            default = 'ssh',
            choices = ['ssh', 'html'],
            help="URL to use for clone")
    subparser.set_defaults(func = clone_script)

    if args:
        args = parser.parse_args(args)
    else:
        args = parser.parse_args()

    args.func(args)
