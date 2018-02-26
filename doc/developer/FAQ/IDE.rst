How to configure my :abbr:`IDE (Integrated Development Environment) ?
#####################################################################

For developers, it can be convenient to use an `IDE <https://en.wikipedia.org/wiki/Integrated_development_environment>`_.
Currently, each repository can be used with:

* **Sublime Text** using the :code:`<REPOSITORY>.sublime-project` files, where :code:`<REPOSITORY>` denote the name of the repository (in lowercase).
  To add a **Sublime Text** build system compatible with **StatisKit** repositories, use the following command

  .. code-block:: console

     build_system --editor=sublime_text
     
.. note::

   Any other IDE build system proposal is welcome.