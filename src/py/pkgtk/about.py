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
# File authors: Pierre Fernique <pfernique@gmail.com> (8)                        #
#                                                                                #
##################################################################################

from .plugin import PluginManager
from .config import load_config, dump_config

def init_about(repository, **kwargs):
    config = load_config(repository)
    about = config.pop('about', dict())
    if 'name' in kwargs:
        name = kwargs.pop('name')
        if name and not name == '""':
            about['name'] = name
        else:
            about.pop('name', '')
    if 'brief' in kwargs:
        brief = kwargs.pop('brief')
        if brief and not brief == '""':
            about['brief'] = brief
        else:
            about.pop('brief', '')
    if 'homepage' in kwargs:
        homepage = kwargs.pop('homepage')
        if homepage and not homepage == '""':
            about['homepage'] = homepage
        else:
            about.pop('homepage', '')
    if 'plugin' not in about or 'plugin' in kwargs:
        plugin = kwargs.pop('plugin', '')
        if plugin:
            if plugin not in load_about:
                raise ValueError('\'load_about\' has no \'' + plugin + '\' plugin')
            about['plugin'] = plugin
    for name, value in kwargs.iteritems():
        if value:
            about[name] = value
        else:
            about.pop(name, "")
    config['about'] = about
    dump_config(repository, config)
    return config

load_about = PluginManager('pkg.load_about',
        brief = "A plugin manager for loading about from software repositories",
        details = """Authors are used to produce a `AUTHORS.*` file and in source\
                   code file license headers.

                   :Parameter:
                     `repository` (str) - The local path of the repository to consider.

                   :Optional Parameter:
                     `filepath` (str) - The local path of a file within the repository to consided.""")

class About(object):

    def __init__(self, name, brief, homepage, version, authors, email):
        if name:
            self.name = name
        else:
            self.name = ''
        if brief:
            self.brief = brief
        else:
            self.brief = ''
        if homepage:
            self.homepage = homepage
        else:
            self.homepage = ''
        self.version = version
        self.authors = authors
        self.email = email

def dump_about(repository, config):
    about = config['about']
    if 'plugin' in about:
        load_about.plugin = about['plugin']
        result = load_about(repository, config)
        if result.name:
            about['name'] = result.name
        else:
            about.pop('name', '')
        if result.brief:
            about['brief'] = result.brief
        else:
            about.pop('brief', '')
        if result.homepage:
            about['homepage'] = result.homepage
        else:
            about.pop('homepage', '')
        if result.version:
            about['version'] = result.version
        else:
            about.pop('version', '')
        if result.authors:
            about['authors'] = result.authors
        else:
            about.pop('authors', '')
        if result.email:
            about['email'] = result.email
        else:
            about.pop('email', '')
        config['about'] = about
        dump_config(repository, config)
