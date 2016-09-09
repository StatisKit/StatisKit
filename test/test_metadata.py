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
# File authors: Pierre Fernique <pfernique@gmail.com> (4)                        #
#                                                                                #
##################################################################################

import unittest

import setuptools
from functools import wraps

def wrapper(f):
    @wraps(f)
    def setup(*args, **kwargs):
        pass
    return setup

setuptools.setup = wrapper(setuptools.setup)

class TestMetaData(unittest.TestCase):
    """Test functions related to scripts"""

    def test_setup(self):
        execfile('setup.py', globals())