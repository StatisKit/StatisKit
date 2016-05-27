import os
import shutil
import unittest
from path import path

from statiskit.create import adapt_git, create_doc, create_py, create_cpp, create_cpp_py, create


class TestScripts(unittest.TestCase):
    """Test functions related to scripts"""

    @classmethod
    def setUpClass(cls):
        cls.reponame = 'StatisKit-Test'
        os.mkdir(cls.reponame)

    def test_adapt_git(self):
        """Test `adapt_git` function of the module `statiskit.create`"""
        adapt_git(self.reponame)
        for filename in ['README.rst', '.travis.yml', '.gitignore']:
            self.assertTrue(os.path.exists(os.path.join(self.reponame, filename)))

    def test_create_doc(self):
        """Test `create_doc` function of the module `statiskit.create`"""
        create_doc(self.reponame)
        for filename in ['index.rst', 'license.rst']:
            self.assertTrue(os.path.exists(os.path.join(self.reponame, 'doc', filename)))
        for dirname in ['user', 'developper', 'maintener', 'reference']:
            self.assertTrue(os.path.exists(os.path.join(self.reponame, 'doc', dirname, 'index.rst')))

    def test_create_py(self):
        """Test `create_py` function of the module `statiskit.create`"""
        create_py(self.reponame)
        srcname = os.path.join(self.reponame, 'src', 'py')
        dirname = self.reponame.lower().replace('_', '.').replace('-', '.').replace('.', os.sep)
        self.assertTrue(os.path.exists(os.path.join(srcname, dirname)))
        dirname = dirname.split(os.sep)
        for index in range(len(dirname)):
            self.assertTrue(os.path.exists(os.path.join(srcname, *dirname[:index+1]) + os.sep + '__init__.py'))

    def test_create_cpp(self):
        """Test `create_cpp` function of the module `statiskit.create`"""
        create_cpp(self.reponame)
        self.assertTrue(os.path.exists(os.path.join(self.reponame, 'SConstruct')))
        self.assertTrue(os.path.exists(os.path.join(self.reponame, 'src', 'cpp', 'SConscript')))

    def test_create_cpp_py(self):
        """Test `create_cpp_py` function of the module `statiskit.create`"""
        create_cpp_py(self.reponame)
        self.assertTrue(os.path.exists(os.path.join(self.reponame, 'src', 'py', 'SConscript')))

    def test_create(self):
        """Test `create` function of the module `statiskit.create`"""
        filenames = set(create(self.reponame, languages = ['py', 'cpp']))
        for filename in path(self.reponame).walkfiles():
            self.assertIn(str(filename.relpath(self.reponame)), filenames)
        filenames = set(create(self.reponame, []))
        for filename in path(self.reponame).walkfiles():
            self.assertIn(str(filename.relpath(self.reponame)), filenames)

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(cls.reponame)
