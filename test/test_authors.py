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
# File authors: Pierre Fernique <pfernique@gmail.com> (5)                        #
#                                                                                #
##################################################################################

import os
import unittest

from pkgtk.config import init_config
from pkgtk.authors import init_authors, load_authors

class TestAuthors(unittest.TestCase):
    """Test functions related to authoring"""

    @classmethod
    def setUpClass(cls):
        cls.repository = '.'
        init_authors(cls.repository)
        cls.config = init_config(cls.repository)
        os.rename(cls.repository + os.sep + '.pkgtk.yml', cls.repository + os.sep + '.pkgtk.back')
        if 'basename' in cls.config['authors']:
            os.rename(cls.repository + os.sep + cls.config['authors']['basename'], cls.repository + os.sep + cls.config['authors']['basename'] + '.back')

    def test_init(self):
        """Test `init_authors` function of module `pkgtk.authors`"""
        init_authors(self.repository)
        with self.assertRaises(AttributeError):
            init_authors(self.repository, format='{phone}')
        with self.assertRaises(ValueError):
            init_authors(self.repository, plugin='blame')
        init_authors(self.repository, **self.config.get('authors', {}))
        config = init_config(self.repository, **self.config.get('about', {}))
        self.assertDictContainsSubset(config, self.config)

    def test_commit(self):
        """Test `load_authors` function of module `pkgtk.load_authors_commit`"""
        self.assertIn('commit', load_authors)
        load_authors.plugin = 'commit'
        authors = load_authors(self.repository)
        if 'basename' in self.config['authors']:
            with open(self.repository + os.sep + self.config['authors']['basename'] + '.back', 'r') as filehandler:
                previous = filehandler.read()
            current = authors.format(self.config['authors']['format'])
            #self.assertMultiLineEqual(current, previous[-len(current):])

    @classmethod
    def tearDownClass(cls):
        os.rename(cls.repository + os.sep + '.pkgtk.back', cls.repository + os.sep + '.pkgtk.yml')
        if 'basename' in cls.config['authors']:
            os.rename(cls.repository + os.sep + cls.config['authors']['basename'] + '.back', cls.repository + os.sep + cls.config['authors']['basename'])
