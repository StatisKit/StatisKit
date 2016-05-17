#########################################################################
#                                                                       #
#  StatisKit-Core: The StatisKit-Core package provides data,            #
#  distribution and estimator classes and methods to perform classical  #
#  statistical analysis in C++ or Python.                               #
#                                                                       #
#  Copyright (c) 2016 INRA, CIRAD, Inria                                #
#                                                                       #
#  This software is distributed under the CeCILL-C license. You should  #
#  have received a copy of the legalcode along with this work. If not,  #
#  see  <http://www.cecill.info/licences/Licence_CeCILL-C_V1-en.html>.  #
#                                                                       #
#  File author: Pierre Fernique <pfernique@gmail.com> (8)               #
#                                                                       #
#########################################################################

try:
    import pkg_resources
    pkg_resources.declare_namespace(__name__)
except ImportError:
    import pkgutil
    __path__ = pkgutil.extend_path(__path__, __name__)
