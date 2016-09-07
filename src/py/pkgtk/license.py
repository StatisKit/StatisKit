##################################################################################
#                                                                                #
# PkgTk: Toolkit for packaging                                                   #
#                                                                                #
# Homepage: pkgtk.readthedocs.io                                                 #
#                                                                                #
# This software is distributed under the CeCILL-C license. You should have       #
# received a copy of the legalcode along with this work. If not, see             #
# <http://www.cecill.info/licences/Licence_CeCILL-C_V1-en.html>.                 #
#                                                                                #
# File authors: Pierre Fernique <pfernique@gmail.com> (3)                        #
#                                                                                #
##################################################################################

import itertools
import textwrap
import os
import fnmatch

from path import path

from .plugin import PluginManager
from .config import load_config, dump_config
from .languages import get_language

def init_license(repository, **kwargs):
    config = load_config(repository)
    license = config.pop('license', dict())
    if 'basename' not in license or 'basename' in kwargs:
        basename = kwargs.pop('basename', '')
        if not basename:
            basename = 'LICENSE.rst'
        license['basename'] = basename
    if 'plugin' not in license or 'plugin' in kwargs:
        plugin = kwargs.pop('plugin', '')
        if plugin not in load_license:
            raise ValueError('\'load_license\' has no \'' + plugin + '\' plugin')
        license['plugin'] = plugin
    if 'width' not in license or 'width' in kwargs:
        license['width'] = int(kwargs.pop('width', 78))
    else:
        license['width'] = int(license.pop('width'))
    config['license'] = license
    dump_config(repository, config)

load_license = PluginManager('pkgtk.load_license',
        brief = "A plugin manager for loading license from software repositories",
        details = """License is used to produce a `LICENSE.*` file and in source\
                   code file license headers.

                   :Parameters:
                    - `filepath` (None|str) - The local path of a file within the repository to consided.
                                              If set to `None`, a `LICENSE.*` file content is generated,
                                              otherwise a license header content is generated.
                    - `repository` (str) -
                    - `config` (dict) - """)

def remove_license(filepath, delimiters):
    if not len(delimiters) == 3:
        raise ValueError()
    if any(len(delimiter) == 0 for delimiter in delimiters):
        raise ValueError()
    if not len(delimiters[1]) == 1 or delimiters[1].isspace():
        raise ValueError()
    has = False
    stop = False
    with open(filepath, 'r') as filehandler:
        content = filehandler.read()
        index = 0
        has = content[index:index+len(delimiters[0])] == delimiters[0]
        if has:
            index += len(delimiters[0])
            while content[index:index+len(delimiters[1])] == delimiters[1] and not content[index:index+len(delimiters[2])+1] == delimiters[2] + '\n':
                index += len(delimiters[1])
            has = content[index:len(delimiters[2])+index] == delimiters[2]
            if has:
                index += len(delimiters[2])
            while not stop and has and content[index+1:index+1+len(delimiters[0])] == delimiters[0]:
                index += len(delimiters[0]) + 1
                stop = True
                while index < len(content) and not content[index:index+len(delimiters[2])+1] == delimiters[2] + '\n' and not content[index] == '\n':
                    stop = stop and content[index:index+len(delimiters[1])] == delimiters[1]
                    index += 1
                has = index < len(content) and content[index:index+len(delimiters[2])] == delimiters[2]
                if has:
                    index += len(delimiters[2])
    if has and stop:
        while index < len(content) and content[index] == '\n':
            index += 1
        content = content[index:]
    return content

def dump_license(repository, config):
    load_license.plugin = config['license']['plugin']
    with open(repository + os.sep + config['license']['basename'], 'w') as filehandler:
        filehandler.write(load_license(repository, None, config=config))
    exclude = config['license'].get('exclude', [])
    for filepath in path(repository).walkfiles():
        language = get_language(filepath)
        if language and not any(fnmatch.fnmatch(filepath, pattern) for pattern in exclude):
            if 'delimiters' not in config['license'] or language not in config['license']['delimiters']:
                if language in ['C', 'C++']:
                    delimiters = ['/*', '*', '*/']
                elif language in ['Python', 'YAML']:
                    delimiters = ['#'] * 3
                elif language == 'reStructuredText':
                    delimiters = ['.. ', '.', ' ..']
                else:
                    raise ValueError()
            else:
                delimiters = config['license']['delimiters'][language]
            if not len(delimiters) == 3:
                raise ValueError()
            if any(len(delimiter) == 0 for delimiter in delimiters):
                raise ValueError()
            if not len(delimiters[1]) == 1 or delimiters[1].isspace():
                raise ValueError()
            content = remove_license(filepath, delimiters)
            width = config['license']['width']
            header = []
            for line in load_license(repository, filepath, config=config).splitlines(True):
                if not line.isspace():
                    for subline in itertools.chain(*[textwrap.wrap(line, width) if not line.isspace() else [" "]]):
                        header.append(delimiters[0] + " " + ("{:" + str(width) + "}").format(subline) + " " + delimiters[-1])
                else:
                    header.append(delimiters[0] + " " +  ("{:" + str(width) + "}").format(" ") + " " + delimiters[-1])
            header = [delimiters[0] + delimiters[1] * (width + 2) + delimiters[-1],
                      delimiters[0] + ' ' * (width + 2) + delimiters[-1]] + header
            header.append(delimiters[0] + ' ' * (width + 2) + delimiters[-1])
            header.append(delimiters[0] + delimiters[1] * (width + 2) + delimiters[-1])
            with open(filepath, 'w') as filehandler:
                filehandler.write('\n'.join(header) + '\n\n' + content)
