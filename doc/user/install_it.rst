Install it !
############

.. _section-user-install_it-prerequisites:

Prerequisites
=============

In order to ease the installation of the **StatisKit** software suite on multiple operating systems, the **Conda** package and environment management system is used.

.. note::

    For more information concerning **Conda**, please refers to its `documentation <http://conda.pydata.org/docs>`_.

To install conda, please refers to this `page <https://conda.io/docs/user-guide/install/index.html>`_.
Installers for:

* **Miniconda** are available on this `page <https://conda.io/miniconda.html>`_.
* **Anaconda** are available on this `page <https://www.anaconda.com/download/>`_.

.. note::

    We recommand to follow the instruction for silent installation and to pay attention to the :code:`PATH` environement variable.

.. warning::

    In the following, it is assumed that the **Conda** :code:`activate` scripts are available from the command line.

Recommanded Installation
========================

Recommanded installation relie on **Conda** environment.
You can download an environment with the :code:`anaconda-client`.
If you don't have this package installed, it can be done using the following command line:
    
.. code-block:: console

    conda install -n root anaconda-client

Then, choose an interface and proceed as detailled the corresponding section:

.. toctree::
    :maxdepth: 1

    c++
    python


Custom Installations
====================
    
For custom installations, **Conda** environments proposed in the :ref:`section-recommended-installation` section can be adapted to fit your purposes.
For example, if you consider the *Python* interface, the environment is described as follows:

.. remote-code-block:: yaml

    https://raw.githubusercontent.com/StatisKit/python-binder/master/environment.yml
    
If you want :

* To change the name of the environment in which this interface is installed (e.g. :code:`python` in place of :code:`python-statiskit`), replace the name field by the appropriate name using the following command in a shell:

  .. code-block:: console

    conda env update -n python statiskit/python-statiskit

* To remove a precise package of the environment, download the environment and remove the package name from the listing.
  If this package is mandatory for the packages you kept, don't worry, **Conda** will ensure that it is nevertheless installed. 
  
  .. note::
  
    You can download an environment with the :code:`anaconda-client`.
    If you don't have this package installed, it can be done using the following command line:
    
    .. code-block:: console
    
        conda install -n root anaconda-client
        
    Then, download the :code:`python-statiskit` environment using the following command line:
    
    .. code-block:: console
    
        anaconda download statiskit/python-statiskit
        
    Edit the :code:`environment.yml` file downloaded and install the resulting environment:
     
    .. code-block:: console

        conda env update

.. warning::

    If you are not in the same shell, **Conda** is likely to be inactivated.
    To reactivate it, follow instructions available in :ref:`section-activate-conda` the section.
