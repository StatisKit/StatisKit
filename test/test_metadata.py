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
# File authors: Pierre Fernique <pfernique@gmail.com> (10)                       #
#                                                                                #
##################################################################################

import sys
import unittest

import setuptools
from setuptools import sandbox
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