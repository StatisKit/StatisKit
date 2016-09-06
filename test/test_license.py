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
# File authors: Pierre Fernique <pfernique@gmail.com> (22)                       #
#                                                                                #
##################################################################################

import os
import git
import unittest
import tempfile

from pkgtk.config import init_config
from pkgtk.license import init_license, load_license, dump_license

class TestLicence(unittest.TestCase):
    """Test functions related to licensing"""

    @classmethod
    def setUpClass(cls):
        cls.repository = '.'
        init_license(cls.repository, plugin='CeCILL-C')
        cls.config = init_config(cls.repository)
        os.rename(cls.repository + os.sep + '.pkgtk.yml', cls.repository + os.sep + '.pkgtk.back')
        os.rename(cls.repository + os.sep + cls.config['license']['basename'], cls.repository + os.sep + cls.config['license']['basename'] + '.back')

    def test_init(self):
        """Test `init_license` function of module `pkgtk.license`"""
        init_license(self.repository, plugin='CeCILL-C')
        init_license(self.repository)

    def test_load_cecillc(self, plugin='CeCILL-C'):
        """Test `load_license` function of module `pkgtk.load_license_cecillc`"""
        load_license.plugin = plugin
        dump_license(self.repository, None, self.config)
        with open(self.repository + os.sep + self.config['license']['basename'], 'r') as filehandler:
            curr = filehandler.read()
        with open(self.repository + os.sep + self.config['license']['basename'] + '.back', 'r') as filehandler:
            prev = filehandler.read()
        self.assertMultiLineEqual(curr, prev)

    def test_dump_cecillc_c(self, plugin='CeCILL-C', suffixes=['.c', '.h']):
        """Test `dump_license` function of module `pkgtk.license` for C files"""
        load_license.plugin = plugin
        repo = git.Repo('.')
        for suffix in suffixes:
            with tempfile.NamedTemporaryFile(suffix=suffix, mode='r', dir=self.repository) as filehandler:
                repo.index.add([filehandler.name])
                repo.index.commit('Add ' + filehandler.name)
                dump_license(self.repository, filehandler.name, self.config)
                content = filehandler.read()
                dump_license(self.repository, filehandler.name, self.config)
                filehandler.seek(0)
                repo.head.reference = repo.commit('HEAD~1')
                repo.index.reset()
                self.assertMultiLineEqual(content, filehandler.read())

    def test_dump_cecillc_cpp(self):
        """Test `dump_license` function of module `pkgtk.license` for C++ files"""
        self.test_dump_cecillc_c(suffixes=['.cpp', '.cxx', '.c++', '.hpp', '.hxx', '.h++'])

    def test_dump_cecillc_py(self):
        """Test `dump_license` function of module `pkgtk.license` for Python files"""
        self.test_dump_cecillc_c(suffixes=['.py'])

    def test_dump_cecillc_rst(self):
        """Test `dump_license` function of module `pkgtk.license` for reStructuredText files"""
        self.test_dump_cecillc_c(suffixes=['.rst'])

    @classmethod
    def tearDownClass(cls):
        os.rename(cls.repository + os.sep + '.pkgtk.back', cls.repository + os.sep + '.pkgtk.yml')
        os.rename(cls.repository + os.sep + cls.config['license']['basename'] + '.back', cls.repository + os.sep + cls.config['license']['basename'])
