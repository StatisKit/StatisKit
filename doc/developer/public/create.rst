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
           description="See :ref:`create_initialize` section. The repository |br|
                        initialization create an empty repository in the **StatisKit** |br|
                        organization."];
        B [label = "Complete", shape="roundedbox",
           description="See :ref:`create_complete` section. In order to complete |br|
                        the empty repository, you must respect some guidelines |br|
                        concering repository structures and mandatory files."];
        C [label = "Activate", shape="roundedbox",
           description="See :ref:`create_activate` section. In order to enable |br|
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
