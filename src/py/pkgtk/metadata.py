##################################################################################
#                                                                                #
# PkgTk: Tool kit for Python packages                                            #
#                                                                                #
# Homepage: http://pkgtk.readthedocs.io                                          #
#                                                                                #
# This software is distributed under the CeCILL-C license. You should have       #
# received a copy of the legalcode along with this work. If not, see             #
# <http://www.cecill.info/licences/Licence_CeCILL-C_V1-en.html>.                 #
#                                                                                #
# File authors: Pierre Fernique <pfernique@gmail.com> (2)                        #
#                                                                                #
##################################################################################

import copy

from .config import load_config, dump_config
from .about import dump_about

class MetaData(object):

    def __init__(self, repository):
        self._repository = repository
        self._config = load_config(self._repository)
        if 'about' in self._config:
            self.__config = copy.deepcopy(self._config)
            dump_about(self._repository, self._config)

    def __del__(self):
        if hasattr(self, '__config'):
            dump_config(self._repository, self.__config)

    @property
    def name(self):
        return self._config.get('about', dict()).get('name', '')

    @property
    def version(self):
        return self._config.get('about', dict()).get('version', None)

    @property
    def authors(self):
        return ', '.join(self._config.get('about', dict()).get('authors', []))

    @property
    def email(self):
        return self._config.get('about', dict()).get('email', '')

    @property
    def description(self):
        return self._config.get('about', dict()).get('brief', '')

    @property
    def long_description(self):
        details = self._config.get('about', dict()).get('details', None)
        if not details:
            details = path.path(self._repository).files('README.*')
            if details:
                details = details.pop()
        if details:
            with open(self._repository + os.sep + details, 'r') as filehandler:
                content = filehandler.read()
            return content
        else:
            return ''

    @property
    def license(self):
        return self._config.get('license', dict()).get('plugin', None)

def load_metadata(repository):
    return MetaData(repository)
