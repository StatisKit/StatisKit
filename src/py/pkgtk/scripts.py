##################################################################################
#                                                                                #
# MngIt: Manage redundant information in software                                #
#                                                                                #
# Copyright (c) 2016 Pierre Fernique                                             #
#                                                                                #
# This software is distributed under the CeCILL-C license. You should have       #
# received a copy of the legalcode along with this work. If not, see             #
# <http://www.cecill.info/licences/Licence_CeCILL-C_V1-en.html>.                 #
#                                                                                #
# File authors: Pierre Fernique <pfernique@gmail.com> (6)                        #
#                                                                                #
##################################################################################

from argparse import ArgumentParser, RawTextHelpFormatter

from pkgtk.config import init_config
from pkgtk.authors import init_authors, load_authors, dump_authors

def authors_script(args):
    """Add the authors option in the configuration file"""
    kwargs = dict()
    if args.root:
        root = args.root
    else:
        root = '.'
    if args.basename:
        kwargs['basename'] = args.basename
    if args.format:
        kwargs['format'] = args.format
    if args.plugin:
        kwargs['plugin'] = args.plugin
    init_authors(root, **kwargs)
    config = init_config(root)
    dump_authors(root, config)

def pkgtk(args=None):
    parser = ArgumentParser(description='Software manager',
            formatter_class=RawTextHelpFormatter)

    subparsers = parser.add_subparsers(title="These are the pkgit commands used in various situations")

    subparser = subparsers.add_parser('authors', help="Handle file authors")
    subparser.add_argument('--root', type=str, default='',
            help="Root directory of the repository")
    subparser.add_argument('--basename', type=str, default='',
            help="Basename to use")
    subparser.add_argument('--format', type=str, default='',
            help="Format to use")
    subparser.add_argument('--plugin', type=str, default='',
            help="Plugin to use",
            choices=list(load_authors))
    subparser.set_defaults(func = authors_script)

    if args:
        args = parser.parse_args(args)
    else:
        args = parser.parse_args()

    args.func(args)
