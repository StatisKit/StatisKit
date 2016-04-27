from setuptools import setup, find_packages

packages = find_packages("src")
package_dir = {package : "src" for package in packages}

setup(name = "PluginTools",
      version = "0.1.0",
      packages = packages,
      package_dir = {"" : "src"},
      author = 'Pierre Fernique',
      entry_points = {'plugintools.hello_world' : 'en = plugintools.hello_world_en:hello_world'})
