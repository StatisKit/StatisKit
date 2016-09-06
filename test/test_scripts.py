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
# File authors: Pierre Fernique <pfernique@gmail.com> (29)                       #
#                                                                                #
##################################################################################

import os
import unittest
import subprocess

from pkgtk.config import load_config
from pkgtk.scripts import pkgtk

class TestScripts(unittest.TestCase):
    """Test functions related to scripts"""

    @classmethod
    def setUpClass(cls):
        cls.repository = '.'
        cls.config = load_config(cls.repository)
        os.rename(cls.repository + os.sep + '.pkgtk.yml', cls.repository + os.sep + '.pkgtk.back')
        if 'basename' in cls.config['authors']:
            os.rename(cls.repository + os.sep + cls.config['authors']['basename'], cls.repository + os.sep + cls.config['authors']['basename'] + '.back')

    def test_authors(self):
        """Test `pkgtk authors` script of module `pkgtk.scripts`"""
        pkgtk(['authors'])
        pkgtk(['authors']+['--' + key + '=' + str(value) for key, value in self.config['authors'].iteritems()])

    def test_about(self):
        """Test `pkgtk about` script of module `pkgtk.scripts`"""
        pkgtk(['about'])
        pkgtk(['about']+['--' + key + '=' + str(value) for key, value in self.config['about'].iteritems()])

    @classmethod
    def tearDownClass(cls):
        os.rename(cls.repository + os.sep + '.pkgtk.back', cls.repository + os.sep + '.pkgtk.yml')
        if 'basename' in cls.config['authors']:
            os.rename(cls.repository + os.sep + cls.config['authors']['basename'] + '.back', cls.repository + os.sep + cls.config['authors']['basename'])