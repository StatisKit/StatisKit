##################################################################################
#                                                                                #
# StatisKit: meta-repository providing general documentation and tools for the   #
# **StatisKit** Organization                                                     #
#                                                                                #
# Copyright (c) 2016 Pierre Fernique                                             #
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
import subprocess

from statiskit.scripts import statiskit


class TestScripts(unittest.TestCase):
    """Test functions related to scripts"""

    @classmethod
    def setUpClass(cls):
        pass

    def test_create(self):
        """Test `statiskit create` script of module `statiskit.scripts`"""
        pass

    @classmethod
    def tearDownClass(cls):
        pass
