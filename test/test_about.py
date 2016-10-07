##################################################################################
#                                                                                #
# PkgTk: Tool kit for Python packages                                            #
#                                                                                #
# Homepage: pkgtk.readthedocs.io                                                 #
#                                                                                #
# Copyright (c) 2016 Pierre Fernique                                             #
#                                                                                #
# This software is distributed under the CeCILL-C license. You should have       #
# received a copy of the legalcode along with this work. If not, see             #
# <http://www.cecill.info/licences/Licence_CeCILL-C_V1-en.html>.                 #
#                                                                                #
# File authors: Pierre Fernique <pfernique@gmail.com> (3)                        #
#                                                                                #
##################################################################################

import os
import unittest

from pkgtk.config import init_config
from pkgtk.about import init_about, dump_about

class TestLicence(unittest.TestCase):
    """Test functions related to licensing"""

    @classmethod
    def setUpClass(cls):
        cls.repository = '.'
        cls.config = init_config(cls.repository)
        os.rename(cls.repository + os.sep + '.pkgtk.yml', cls.repository + os.sep + '.pkgtk.back')

    def test_init_github(self, plugin='github'):
        """Test `init_about` function of module `pkgtk.about`"""
        init_about(self.repository, plugin=plugin)
        init_about(self.repository)

    def test_load_dump_github(self, plugin='github'):
        """Test `dump_about` function of module `pkgtk.about`"""
        self.config['about'].clear()
        self.config['about']['plugin'] = plugin
        dump_about(self.repository, self.config)
        os.unlink(self.repository + os.sep + '.pkgtk.yml')

    @classmethod
    def tearDownClass(cls):
        os.unlink(cls.repository + os.sep + '.pkgtk.yml')
        os.rename(cls.repository + os.sep + '.pkgtk.back', cls.repository + os.sep + '.pkgtk.yml')
