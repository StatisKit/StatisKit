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
# File authors: Pierre Fernique <pfernique@gmail.com> (10)                       #
#                                                                                #
##################################################################################

import os
import git
import unittest
import hashlib
import __builtin__
import path

from tempfile import NamedTemporaryFile
from pkgtk.config import init_config
from pkgtk.license import init_license, load_license, dump_license

class TemplateRender(object):

    def __get__(self, obj, objtype, **kwargs):
        code = obj.code
        code = code.replace('\n    __M_caller = context.caller_stack._push_frame()', '', 1)
        code = code.replace('\n    __M_caller = context.caller_stack._push_frame()', '', 1)
        code = code.replace("        return ''\n    finally:\n        context.caller_stack._pop_frame()\n", "        return __M_string\n    except:\n        return ''", 1)
        code = code.replace("context,**pageargs", "**context", 1)
        code = code.replace("\n        __M_locals = __M_dict_builtin(pageargs=pageargs)", "", 1)
        code = code.replace("__M_writer = context.writer()", "__M_string = u''")
        code = code.replace("__M_writer(", "__M_string = operator.add(__M_string, ")
        code = "import operator\n" + code
        exec(code, globals())
        def __call__(**context):
            for builtin in dir(__builtin__):
                if not builtin in context:
                    context[builtin] = getattr(__builtin__, builtin)
            return globals()["render_body"](**context)
        return __call__

from mako.template import Template
Template.render = TemplateRender()

class TestLicence(unittest.TestCase):
    """Test functions related to licensing"""

    @classmethod
    def setUpClass(cls):
        cls.repository = '.'
        init_license(cls.repository, plugin='CeCILL-C')
        cls.config = init_config(cls.repository)
        cls.config['license']['exclude'] += path.path(cls.repository).walkfiles()
        os.rename(cls.repository + os.sep + '.pkgtk.yml', cls.repository + os.sep + '.pkgtk.back')
        os.rename(cls.repository + os.sep + cls.config['license']['basename'], cls.repository + os.sep + cls.config['license']['basename'] + '.back')

    def test_init(self):
        """Test `init_license` function of module `pkgtk.license`"""
        init_license(self.repository, plugin='CeCILL-C')
        init_license(self.repository)

    def test_load_dump_cecillc(self, plugin='CeCILL-C'):
        """Test `dump_license` function of module `pkgtk.license`"""
        load_license.plugin = plugin
        repo = git.Repo('.')
        commit = repo.commit('HEAD')
        author = git.Actor('John Doe', 'jdoe@host')
        tempfiles = []
        for suffix in ['.c', '.h', '.cpp', '.cxx', '.c++', '.hpp', '.hxx', '.h++', '.py', '.rst', '.yml', '.yaml']:
            with NamedTemporaryFile(suffix=suffix, mode='w', dir=self.repository, delete=False) as filehandler:
                tempfiles.append(filehandler.name)
        repo.index.add(tempfiles)
        repo.index.commit('Add ' + ', '.join(tempfile for tempfile in tempfiles), author=author)
        dump_license(self.repository, self.config)
        repo.index.add(tempfiles)
        author.name = ' '.join(reversed(author.name.split()))
        repo.index.commit('Add ' + ', '.join(tempfile for tempfile in tempfiles), author=author)
        dump_license(self.repository, self.config)
        md5sum = hashlib.md5()
        for tempfile in tempfiles:
            with open(tempfile, 'r') as filehandler:
                md5sum.update(filehandler.read())
        dump_license(self.repository, self.config)
        _md5sum = hashlib.md5()
        for tempfile in tempfiles:
            with open(tempfile, 'r') as filehandler:
                _md5sum.update(filehandler.read())
        repo.head.reference = commit
        repo.index.reset()
        for tempfile in tempfiles:
            os.unlink(tempfile)
        self.assertEqual(md5sum.digest(), _md5sum.digest())
        with open(self.repository + os.sep + self.config['license']['basename'], 'r') as filehandler:
            curr = filehandler.read()
        with open(self.repository + os.sep + self.config['license']['basename'] + '.back', 'r') as filehandler:
            prev = filehandler.read()
        self.assertIn(curr, prev)

    @classmethod
    def tearDownClass(cls):
        os.unlink(cls.repository + os.sep + '.pkgtk.yml')
        os.rename(cls.repository + os.sep + '.pkgtk.back', cls.repository + os.sep + '.pkgtk.yml')
        os.unlink(cls.repository + os.sep + cls.config['license']['basename'])
        os.rename(cls.repository + os.sep + cls.config['license']['basename'] + '.back', cls.repository + os.sep + cls.config['license']['basename'])
