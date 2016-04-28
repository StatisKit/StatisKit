import unittest

from plugintools.functor import PluginFunctor

def make_functor():
    return PluginFunctor('plugintools.hello_world',
                brief = "This is a brief description",
                details = "This is a more detailed description")

class TestFunctor(unittest.TestCase):
    """Test functions related to PluginFunctor"""

    @classmethod
    def setUpClass(cls):
        cls.hello_world = make_functor()

    def test_non_selection(self):
        hello_world = make_functor()
        with self.assertRaises(NotImplementedError):
            hello_world()

    def test_get_and_call(self):
        self.assertIn('en', self.hello_world)
        self.hello_world.plugin = 'en'
        self.assertEqual('hello', self.hello_world())

    def test_set(self):
        def fr():
            return 'salut'
        with self.assertRaises(ValueError):
            self.hello_world.plugin = 'fr'
        self.hello_world['fr'] = fr
        self.assertIn('fr', self.hello_world)
        self.hello_world.plugin = 'fr'
        self.assertEqual('salut', self.hello_world())
        with self.assertRaises(TypeError):
            self.hello_world[0] = fr
        with self.assertRaises(ValueError):
            self.hello_world['us'] = 'us'
        with self.assertRaises(ValueError):
            self.hello_world['en'] = 'en'
        with self.assertRaises(TypeError):
            self.hello_world['fr'] = 0

    def test_alias(self):
        self.hello_world['us'] = 'en'
        self.assertIn('us', self.hello_world)
        self.hello_world.plugin = 'us'
        self.assertEqual('hello', self.hello_world())

    def test_doc(self):
        hello_world = make_functor()
        hello_world['us'] = 'en'
        self.assertMultiLineEqual("""This is a brief description

This is a more detailed description

:Available Implementations:
 - 'en'
 - 'us'""", hello_world.__doc__)
