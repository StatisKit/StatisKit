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

import unittest

from pkg.plugin import PluginManager, ProxyManager

class Hello(object):

    @staticmethod
    def hello():
        return "hello"

class Salut(object):

    @staticmethod
    def salut():
        return "salut"

class TestPlugin(unittest.TestCase):
    """Test functions related to :mod:`pkg.plugin`"""

    @classmethod
    def setUpClass(cls):
        cls.proxy_manager = ProxyManager('pkg.proxytest',
                                         brief = "This is a brief description",
                                         details = "This is a more detailed description")
        cls.proxy_manager['en'] = Hello

        cls.plugin_manager = PluginManager('pkg.plugintest',
                                           brief = "This is a brief description",
                                           details = "This is a more detailed description")
        cls.plugin_manager['en'] = Hello.hello

    def test_proxy_non_selection(self):
        del self.proxy_manager.proxy
        with self.assertRaises(NotImplementedError):
            self.proxy_manager()

    def test_proxy_get_call(self):
        self.assertIn('en', self.proxy_manager)
        self.proxy_manager.proxy = 'en'
        self.assertEqual(Hello, self.proxy_manager())

    def test_proxy_set(self):
        with self.assertRaises(ValueError):
            self.proxy_manager.proxy = 'fr'
        self.proxy_manager['fr'] = Salut
        self.assertIn('fr', self.proxy_manager)
        self.proxy_manager.proxy = 'fr'
        self.assertEqual(Salut, self.proxy_manager())
        with self.assertRaises(TypeError):
            self.proxy_manager[0] = Salut
        with self.assertRaises(ValueError):
            self.proxy_manager['us'] = 'us'
        with self.assertRaises(ValueError):
            self.proxy_manager['en'] = 'en'
        with self.assertRaises(TypeError):
            self.proxy_manager['fr'] = 0

    def test_proxy_alias(self):
        self.proxy_manager['us'] = 'en'
        self.assertIn('us', self.proxy_manager)
        self.proxy_manager.proxy = 'us'
        self.assertEqual(Hello, self.proxy_manager())

    def test_proxy_doc(self):
        self.assertMultiLineEqual("""This is a brief description

This is a more detailed description

:Available Implementations:
 - 'en'
 - 'us'""", self.proxy_manager.__doc__)

    def test_plugin_non_selection(self):
        del self.plugin_manager.plugin
        with self.assertRaises(NotImplementedError):
            self.plugin_manager()

    def test_plugin_get_call(self):
        self.assertIn('en', self.plugin_manager)
        self.plugin_manager.plugin = 'en'
        self.assertEqual('hello', self.plugin_manager())

    def test_plugin_set(self):
        with self.assertRaises(ValueError):
            self.plugin_manager.plugin = 'fr'
        self.plugin_manager['fr'] = Salut.salut
        self.assertIn('fr', self.plugin_manager)
        self.plugin_manager.plugin = 'fr'
        self.assertEqual('salut', self.plugin_manager())
        with self.assertRaises(TypeError):
            self.plugin_manager[0] = Salut.salut
        with self.assertRaises(ValueError):
            self.plugin_manager['us'] = 'us'
        with self.assertRaises(ValueError):
            self.plugin_manager['en'] = 'en'
        with self.assertRaises(TypeError):
            self.plugin_manager['fr'] = 0

    def test_plugin_alias(self):
        self.plugin_manager['us'] = 'en'
        self.assertIn('us', self.plugin_manager)
        self.plugin_manager.plugin = 'us'
        self.assertEqual('hello', self.plugin_manager())

    def test_plugin_doc(self):
        self.assertMultiLineEqual("""This is a brief description

This is a more detailed description

:Available Implementations:
 - 'en'
 - 'us'""", self.plugin_manager.__doc__)
