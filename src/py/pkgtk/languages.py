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
# File authors: Pierre Fernique <pfernique@gmail.com> (4)                        #
#                                                                                #
##################################################################################

import os

def get_language(basename):
    ext = os.path.splitext(basename)[-1].lower()
    if ext:
        if ext in ['.h', '.c']:
            return 'C'
        elif ext in ['.hxx','.hpp', '.h++', '.cxx', '.cpp', '.c++']:
            return 'C++'
        elif ext in ['.py']:
            return 'Python'
        elif ext in ['.yaml', '.yml']:
            return 'YAML'
        elif ext in ['.rst']:
            return 'reStructuredText'
        elif ext in ['.md', '.markdown']:
            return 'Markdown'
    else:
        if basename in ['SConscript', 'SConstruct']:
            return 'Python'
