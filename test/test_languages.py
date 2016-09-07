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

import unittest

from pkgtk.languages import get_language

class TestLanguages(unittest.TestCase):
    """Test functions related to languages"""

    def test_c(self, language='C', *exts):
        """Test `get_language` function for C files"""
        for ext in exts:
            self.assertEqual(language, get_language('file.' + ext))

    def test_cpp(self):
        """Test `get_language` function for C++ files"""
        self.test_c('C++', 'cpp', 'cxx', 'c++', 'hpp', 'hxx', 'h++')

    def test_python(self):
        """Test `get_language` function for Python files"""
        self.test_c('Python', 'py')

    def test_yaml(self):
        """Test `get_language` function for Python files"""
        self.test_c('YAML', 'yml', 'yaml')

    def test_rst(self):
        """Test `get_language` function for reStructuredText files"""
        self.test_c('reStructuredText', 'rst')

    def test_md(self):
        """Test `get_language` function for Markdown files"""
        self.test_c('Markdown', 'md', 'markdown')
