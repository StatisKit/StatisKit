.. ................................................................................ ..
..                                                                                  ..
..  StatisKit: meta-repository providing general documentation and tools for the    ..
..  **StatisKit** Organization                                                      ..
..                                                                                  ..
..  Copyright (c) 2016 Pierre Fernique                                              ..
..                                                                                  ..
..  This software is distributed under the CeCILL-C license. You should have        ..
..  received a copy of the legalcode along with this work. If not, see              ..
..  <http://www.cecill.info/licences/Licence_CeCILL-C_V1-en.html>.                  ..
..                                                                                  ..
..  File authors: Pierre Fernique <pfernique@gmail.com> (19)                        ..
..                                                                                  ..
.. ................................................................................ ..

Create a new repository
#######################

.. warning::
    
    Only owners of the **StatisKit** organization can create new repositories.
    
To create a new repository use the :code:`statiskit create` command.
This command launches the following workflow in order to create a new repository on the StatisKit organization.
To perform this, :code:`statiskit create` uses the **PyGithub** package to access `GitHub` interface in `Python`.
    
.. blockdiag::
    :align: center
    :desctable:
    
    blockdiag {

        A [label = "Initialize", shape="roundedbox",
           description="See :ref:`Initialize the repository` section. The repository |br|
                        initialization create an empty repository in the **StatisKit** |br|
                        organization."];
        B [label = "Complete", shape="roundedbox",
           description="See :ref:`Complete the repository` section. In order to complete |br|
                        the empty repository, you must respect some guidelines |br|
                        concering repository structures and mandatory files."];
        C [label = "Activate", shape="roundedbox",
           description="See :ref:`Activate repository services` section. In order to enable |br|
                        code review from mainteners, some web-services must be |br|
                        activated."];
        
        A -> B -> C;
    }

.. |br| raw:: html

   <br />
   
.. toctree::
    :hidden:
    
    initialize/index
    complete/index
    activate/index
