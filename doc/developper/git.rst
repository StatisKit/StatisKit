:abbr:`VCS (Version Control System)` configuration
**************************************************

Git
===

Git is a free and open source distributed :abbr:`VCS (Version Control System)`.
If **Git** is not configured you should configure it for your computer.

.. code-block:: bash

    git config --global user.name "Firstname Lastname"
    git config --global user.email firstname.lastname@domain
    git config --global push.default simple

For more details the reader can refer to the **Git** `getting started page <https://git-scm.com/book/en/v2/Getting-Started-About-Version-Control>`_ or `configuration page <https://git-scm.com/book/en/v2/Customizing-Git-Git-Configuration>`_

.. warning::

    The `--global` argument refers to your computer's configuration.
    This step must be done only once for a computer.

For commits, you can configure the editor used for editing commit messages using the following command line for `Vim <http://www.vim.org/>`_ 
  
.. code-block:: bash
  
    git config --global core.editor vim

.. note::
    
    If you want an editor that is not embedded in the console, it is sometimes required to add some flags.
    For instance: 
    
    * For  `Gedit <https://wiki.gnome.org/Apps/Gedit>`_, you must add the flags :code:`-w -s`.
      
      .. code-block:: bash
      
          git config --global core.editor "gedit -w -s"

    * For `GVim <http://www.vim.org/>`_, you must add the flag :code:`--nofork`.

      .. code-block:: bash
    
          git config --global core.editor "gvim --nofork"


GitHub
======

If you do not have a **GitHub** account you must create one at this `address <https://github.com/>`_.
For contribution to **StatisKit** repositories you doesn't need to be part of the **StatisKit** organization (see :doc:`public/index`).
Yet, if you feel you should, contact `any maintenance team member <https://github.com/orgs/StatisKit/teams/maintenance>`_.
