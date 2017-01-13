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
# File authors: Pierre Fernique <pfernique@gmail.com> (6)                        #
#                                                                                #
##################################################################################

import os
import unittest

from pkg.config import init_config
from pkg.authors import init_authors, load_authors

class TestAuthors(unittest.TestCase):
    """Test functions related to authoring"""

    @classmethod
    def setUpClass(cls):
        cls.repository = '.'
        init_authors(cls.repository)
        cls.config = init_config(cls.repository)
        os.rename(cls.repository + os.sep + '.pkg.yml', cls.repository + os.sep + '.pkg.back')
        if 'basename' in cls.config['authors']:
            os.rename(cls.repository + os.sep + cls.config['authors']['basename'], cls.repository + os.sep + cls.config['authors']['basename'] + '.back')

    def test_init(self):
        """Test `init_authors` function of module `pkg.authors`"""
        init_authors(self.repository)
        with self.assertRaises(AttributeError):
            init_authors(self.repository, format='{phone}')
        with self.assertRaises(ValueError):
            init_authors(self.repository, plugin='blame')
        init_authors(self.repository, **self.config.get('authors', {}))
        config = init_config(self.repository, **self.config.get('about', {}))
        self.assertDictContainsSubset(config, self.config)

    def test_commit(self):
        """Test `load_authors` function of module `pkg.load_authors_commit`"""
        self.assertIn('commit', load_authors)
        load_authors.plugin = 'commit'
        authors = load_authors(self.repository)
        if 'basename' in self.config['authors']:
            with open(self.repository + os.sep + self.config['authors']['basename'] + '.back', 'r') as filehandler:
                previous = filehandler.read()
            current = authors.format(self.config['authors']['format'])
            #self.assertIn(current, previous)

    @classmethod
    def tearDownClass(cls):
        os.unlink(cls.repository + os.sep + '.pkg.yml')
        os.rename(cls.repository + os.sep + '.pkg.back', cls.repository + os.sep + '.pkg.yml')
        if 'basename' in cls.config['authors']:
            os.rename(cls.repository + os.sep + cls.config['authors']['basename'] + '.back', cls.repository + os.sep + cls.config['authors']['basename'])
