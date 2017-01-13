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
# File authors: Pierre Fernique <pfernique@gmail.com> (11)                       #
#                                                                                #
##################################################################################

import os
import unittest

from pkg.config import load_config
from pkg.scripts import pkg

class TestScripts(unittest.TestCase):
    """Test functions related to scripts"""

    @classmethod
    def setUpClass(cls):
        cls.repository = '.'
        cls.config = load_config(cls.repository)
        os.rename(cls.repository + os.sep + '.pkg.yml', cls.repository + os.sep + '.pkg.back')
        if 'basename' in cls.config['authors']:
            os.rename(cls.repository + os.sep + cls.config['authors']['basename'], cls.repository + os.sep + cls.config['authors']['basename'] + '.back')

    def test_authors(self):
        """Test `pkg authors` script of module `pkg.scripts`"""
        pkg(['authors'])
        pkg(['authors']+['--' + key + '=' + str(value) for key, value in self.config['authors'].iteritems()])

    def test_license(self):
        """Test `pkg license` script of module `pkg.scripts`"""
        pkg(['license']+['--' + key + '=' + str(value) for key, value in self.config['license'].iteritems() if not key == 'exclude'])

    def test_about(self):
        """Test `pkg about` script of module `pkg.scripts`"""
        pkg(['about']+['--' + key + '=' + '""' for key, value in self.config['about'].iteritems() if not key == 'plugin'])
        pkg(['about']+['--' + key + '=' + str(value) for key, value in self.config['about'].iteritems()])
        pkg(['about', '--remote=https://github.com/StatisKit/PkgTk.git'])
        pkg(['about', '--remote='])

    @classmethod
    def tearDownClass(cls):
        os.unlink(cls.repository + os.sep + '.pkg.yml')
        os.rename(cls.repository + os.sep + '.pkg.back', cls.repository + os.sep + '.pkg.yml')
        if 'basename' in cls.config['authors']:
            os.unlink(cls.repository + os.sep + cls.config['authors']['basename'])
            os.rename(cls.repository + os.sep + cls.config['authors']['basename'] + '.back', cls.repository + os.sep + cls.config['authors']['basename'])
