##################################################################################
#                                                                                #
# PluginTools: Python plugin system                                              #
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

from setuptools import setup, find_packages

packages = find_packages("src")
package_dir = {package : "src" for package in packages}

setup(name = "PluginTools",
      version = "0.1.0",
      packages = packages,
      package_dir = {"" : "src"},
      author = 'Pierre Fernique',
      entry_points = {'plugintools.hello_world' : 'en = plugintools.hello_world_en:hello_world'})
