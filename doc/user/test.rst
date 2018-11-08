.. Copyright [2017-2018] UMR MISTEA INRA, UMR LEPSE INRA,                ..
..                       UMR AGAP CIRAD, EPI Virtual Plants Inria        ..
.. Copyright [2015-2016] UMR AGAP CIRAD, EPI Virtual Plants Inria        ..
..                                                                       ..
.. This file is part of the StatisKit project. More information can be   ..
.. found at                                                              ..
..                                                                       ..
..     http://statiskit.rtfd.io                                          ..
..                                                                       ..
.. The Apache Software Foundation (ASF) licenses this file to you under  ..
.. the Apache License, Version 2.0 (the "License"); you may not use this ..
.. file except in compliance with the License. You should have received  ..
.. a copy of the Apache License, Version 2.0 along with this file; see   ..
.. the file LICENSE. If not, you may obtain a copy of the License at     ..
..                                                                       ..
..     http://www.apache.org/licenses/LICENSE-2.0                        ..
..                                                                       ..
.. Unless required by applicable law or agreed to in writing, software   ..
.. distributed under the License is distributed on an "AS IS" BASIS,     ..
.. WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or       ..
.. mplied. See the License for the specific language governing           ..
.. permissions and limitations under the License.                        ..

Test it !
#########

In a first stage, you are not compelled to install **StatisKit** on your computer in order to discover its functionalities.
Using **Docker** images, **Binder** servers and **Jupyter** notebooks, we are able to provide pre-installed interfaces with various examples.

.. note::

    For more information refers to :
    
    * The **Jupyter** `documentation <https://jupyter.readthedocs.io/en/latest/index.html>`_.
    * The **Binder** `documentation <http://docs.mybinder.org/>`_.
    * The **Docker** `documentation <https://docs.docker.com/>`_.
    
Online With **Binder**
======================

To reproduce the various examples from a **Binder** server, follow this `link <https://beta.mybinder.org/v2/gh/statiskit/statiskit/master?filepath=share/jupyter/index.ipynb>`_.

    
On Your Computer With **Docker**
================================

To reproduce the various examples with **Docker** use these `images <https://hub.docker.com/r/statiskit/statiskit/tags>`_.
After `installing <https://docs.docker.com/engine/installation/>`_ **Docker**, you can type the following command in a shell:

.. code-block:: console

  docker run -i -t -p 8888:8888 statiskit/statiskit:latest

   
Then, follow the given instructions.

.. warning::

    By default, on some operating systems like Ubuntu, docker require to have administration rights.
    You can, for example, execute the preceeding lines after typing :code:`sudo -i` if you are on Ubuntu or follow these `instructions <https://docs.docker.com/engine/installation/linux/linux-postinstall/>`_.
    
.. note::

  If your port :code:`8888` is already used, replace this number in these command lines and instructions given by another one (e.g., :code:`8889`).

On Your Computer From a SSH Server
==================================

To reproduce the various examples from a **SSH** server, you can type the following commands in a shell:

.. code-block:: console

   ssh -L 8888:localhost:8888 <username>@<servername>
   jupyter notebook --ip='*' --port=8888 --no-browser
    
.. note::

   The username on the **SSH** server (resp. the **SSH** servername) is denoted in the following by :code:`<username>` (resp. :code:`<servername>`).
   Please replace it by the appropriate username (resp. servername).

Then, follow the given instructions.

.. note::

   If your port :code:`8888` is already used, replace this number in these command lines and instructions given by another one (e.g., :code:`8889`).