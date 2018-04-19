.. _section-developer-FAQ-C++:

What is the *C++* Style Guide ?
===============================

.. warning::

   Section under construction.
   Until further notice, please use the Google *C++* `style guide <https://google.github.io/styleguide/cppguide.html>`_

* A repository should contain at most :math:`1` *C++* library.
* The *C++* library source code must be located in the :code:`scr/cpp` directory.
* To install headers of the *C++* library, a developer should use the following command in the repository root

  .. code-block:: console

     scons cpp-dev

* To generate and install the *C++* library binaries, a developer should use the following command in the repository root

  .. code-block:: console

     scons cpp-lib

* The following command

  .. code-block:: console

     scons cpp

  should be equivalent to the following commands

  .. code-block:: console

     scons cpp-dev
     scons cpp-lib

* If the *C++* library is interfaced in any other languages (e.g., *Python* or *R*), the wrappers should be generated using the following command

  .. code-block:: console

     scons autowig

  .. note::

     In this case, guidelines proposed in the **AutoWIG** `documentation <http://autowig.rtfd.io>`_ are of most importance.