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
from pkgtk.about import init_about, load_about, dump_about
from pkgtk.license import init_license, load_license, dump_license

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

def about_script(args):
    """Add the about option in the configuration file"""
    kwargs = dict()
    if args.root:
        root = args.root
    else:
        root = '.'
    if args.name:
        kwargs['name'] = args.name
    if args.brief:
        kwargs['brief'] = args.brief
    if args.homepage:
        kwargs['homepage'] = args.homepage
    if args.plugin:
        kwargs['plugin'] = args.plugin
    if args.remote:
        kwargs['remote'] = args.remote
    init_about(root, **kwargs)
    config = init_config(root)
    dump_about(root, config)

def license_script(args):
    kwargs = dict()
    if args.root:
        root = args.root
    else:
        root = '.'
    if args.basename:
        kwargs['basename'] = args.basename
    if args.plugin:
        kwargs['plugin'] = args.plugin
    if args.width:
        kwargs['width'] = args.width
    init_license(root, **kwargs)
    config = init_config(root)
    dump_license(root, config)

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

    subparser = subparsers.add_parser('about', help="Handle file about")
    subparser.add_argument('--root', type=str, default='',
            help="Root directory of the repository")
    subparser.add_argument('--name', type=str,
            help="Name to use")
    subparser.add_argument('--brief', type=str,
            help="Brief description to use")
    subparser.add_argument('--homepage', type=str,
            help="Homepage to use")
    subparser.add_argument('--plugin', type=str,
            help="Plugin to use",
            choices=list(load_about))
    subparser.add_argument('--remote', type=str,
            help="Remote to use")
    subparser.set_defaults(func = about_script)

    subparser = subparsers.add_parser('license', help="Handle file license")
    subparser.add_argument('--root', type=str, default='',
            help="Root directory of the repository")
    subparser.add_argument('--basename', type=str, default='',
            help="Basename to use")
    subparser.add_argument('--width', type=int,
            help="Basename to use")
    subparser.add_argument('--plugin', type=str,
            help="Plugin to use",
            choices=list(load_license))
    subparser.set_defaults(func = license_script)

    if args:
        args = parser.parse_args(args)
    else:
        args = parser.parse_args()

    args.func(args)
