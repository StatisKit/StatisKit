.. _section-developer-FAQ-python:

What is the *Python* Style Guide ?
==================================

.. warning::

   Section under construction.
   Until further notice, please use the Google *Python* `style guide <http://google.github.io/styleguide/pyguide.html>`_.

* A repository should contain at most :math:`1` *Python* package.
* The *Python* package source code must be located in the :code:`scr/py` directory.
* To install the *Python* package, a developer should use the following command in the repository root

  .. code-block:: console

     scons py

  .. note::

     If this package is an interface of a *C++* library, this command should also generate relevant binaries.