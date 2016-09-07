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
# File authors: Pierre Fernique <pfernique@gmail.com> (2)                        #
#                                                                                #
##################################################################################

import yaml
import os

def init_config(repository, **kwargs):
    """Create a MngIt configuration file

    :Parameters:
     - `name` (str) - Name of the software
     - `brief` (str) - A brief description of the software
    """
    config = load_config(repository)
    dump_config(repository, config)
    return config

def load_config(repository):
    config = repository + os.sep + '.pkgtk.yml'
    if not os.path.exists(config):
        config = dict()
    else:
        with open(config, 'r') as filehandler:
            config = yaml.load(filehandler.read())
    return config

def dump_config(repository, config):
    with open(repository + os.sep + '.pkgtk.yml', 'w') as filehandler:
        filehandler.write(yaml.dump(config, default_flow_style=False))

