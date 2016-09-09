.. ................................................................................ ..
..                                                                                  ..
..  PkgTk: Tool kit for Python packages                                             ..
..                                                                                  ..
..  Homepage: pkgtk.readthedocs.io                                                  ..
..                                                                                  ..
..  Copyright (c) 2016 Pierre Fernique                                              ..
..                                                                                  ..
..  This software is distributed under the CeCILL-C license. You should have        ..
..  received a copy of the legalcode along with this work. If not, see              ..
..  <http://www.cecill.info/licences/Licence_CeCILL-C_V1-en.html>.                  ..
..                                                                                  ..
..  File authors: Pierre Fernique <pfernique@gmail.com> (5)                         ..
..                                                                                  ..
.. ................................................................................ ..

.. _install-source:

Installation from source code
=============================
    
In order to install **PkgTk** from source code we recommand to:

* Download the source code available on *GitHub* (see `Git <https://git-scm.com/>`_ and `GitHub <https://github.com/>`_ websites for more information).

  .. code-block:: bash
  
      git clone https://github.com/StatisKit/PkgTk.git
      cd PkgTk
     
* Use the conda recipes present on this repository (see `conda <http://conda.pydata.org/docs/>`_ website for more information).
 
  .. literalinclude:: ../../conda/build.sh

  .. warning::
 
      Following this procedure do not install *Python* packages in develop mode.