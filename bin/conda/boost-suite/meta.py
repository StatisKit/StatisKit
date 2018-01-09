import os
import yaml
import subprocess
import networkx
import shutil
import re
import itertools

from tempfile import NamedTemporaryFile
from path import Path

NON_HEADER_ONLY = ['atomic',
                   'chrono',
                   'container',
                   'context',
                   'coroutine',
                   'date_time',
                   'filesystem',
                   'graph',
                   'iostreams',
                   'locale',
                   'log',
                   'math',
                   'program_options',
                   'python',
                   'random',
                   'regex',
                   'serialization',
                   'signals',
                   'system',
                   'test',
                   'thread',
                   'timer',
                   'type_erasure',
                   'wave']

# process = subprocess.Popen('git clone --recursive http://github.com/boostorg/boost',
#                                            stdout=subprocess.PIPE,
#                                            stderr=subprocess.PIPE,
#                                            shell=True)
# out, err = process.communicate()

# process = subprocess.Popen('git -C boost checkout boost-1.61.0',
#                            stdout=subprocess.PIPE,
#                            stderr=subprocess.PIPE,
#                            shell=True)
# out, err = process.communicate()

def write_meta(graph=None):

    with open('meta.yaml', "w") as filehandler:
        filehandler.write("""
package:
  name: boost-suite
  version: 1.61.0

source:
  fn: boost_1_61_0.tar.bz2
  sha256: a547bd06c2fd9a71ba1d169d9cf0339da7ebf4753849a8f7d6fdb8feee99b640
  url: http://sourceforge.net/projects/boost/files/boost/1.61.0/boost_1_61_0.tar.bz2

build:
  number: 0

requirements:
  build:
    - python
    - libtoolchain
    - python
    - icu 58.*          [unix]
    - bzip2             [unix]
    - zlib

about:
  home: http://www.boost.org/
  license: Boost-1.0
  summary: Boost provides free peer-reviewed portable C++ source libraries.

test:
  requires:
    - libtoolchain
    - python

outputs:
  - name: libboost_atomic                                              [py2k]
    files:                                                             [py2k]
      - lib/libboost_atomic*                               [not win and py2k]
      - Library\lib\\boost_atomic*                              [win and py2k]
      - Library\lib\libboost_atomic*                           [win and py2k]
      - Library\\bin\\boost_atomic*                              [win and py2k]
    requirements:                                                      [py2k]
      run_exports:                                                     [py2k]
        - {{ pin_subpackage("libboost_atomic", exact=True) }}          [py2k]
  - name: libboost_chrono                                              [py2k]
    files:                                                             [py2k]
      - lib/libboost_chrono*                               [not win and py2k]
      - Library\lib\\boost_chrono*                              [win and py2k]
      - Library\lib\libboost_chrono*                           [win and py2k]
      - Library\\bin\\boost_chrono*                              [win and py2k]
    requirements:                                                      [py2k]
      run:                                                             [py2k]
        - {{ pin_subpackage("libboost_system", exact=True) }}          [py2k]
      run_exports:                                                     [py2k]
        - {{ pin_subpackage("libboost_chrono", exact=True) }}          [py2k]
  - name: libboost_container                                           [py2k]
    files:                                                             [py2k]
      - lib/libboost_container*                            [not win and py2k]
      - Library\lib\\boost_container*                           [win and py2k]
      - Library\lib\libboost_container*                        [win and py2k]
      - Library\\bin\\boost_container*                           [win and py2k]
    requirements:                                                      [py2k]
      run_exports:                                                     [py2k]  
        - {{ pin_subpackage("libboost_container", exact=True) }}       [py2k]
  - name: libboost_context                                             [py2k]
    files:                                                             [py2k]
      - lib/libboost_context*                              [not win and py2k]
      - Library\lib\\boost_context*                             [win and py2k]
      - Library\lib\libboost_context*                          [win and py2k]
      - Library\\bin\\boost_context*                             [win and py2k]
  - name: libboost_coroutine                                           [py2k]
    files:                                                             [py2k]
      - lib/libboost_coroutine*                            [not win and py2k]
      - Library\lib\\boost_coroutine*                           [win and py2k]
      - Library\lib\libboost_coroutine*                        [win and py2k]
      - Library\\bin\\boost_coroutine*                           [win and py2k]
    requirements:                                                      [py2k]
      run_exports:                                                     [py2k]
        - {{ pin_subpackage("libboost_coroutine", exact=True) }}       [py2k]
      run:                                                             [py2k]
        - {{ pin_subpackage("libboost_system", exact=True) }}          [py2k]
        - {{ pin_subpackage("libboost_chrono", exact=True) }}          [py2k]
        - {{ pin_subpackage("libboost_thread", exact=True) }}          [py2k]
        - {{ pin_subpackage("libboost_context", exact=True) }}         [py2k]
  - name: libboost_date_time                                           [py2k]
    files:                                                             [py2k]
      - lib/libboost_date_time*                            [not win and py2k]
      - Library\lib\\boost_date_time*                           [win and py2k]
      - Library\lib\libboost_date_time*                        [win and py2k]
      - Library\\bin\\boost_date_time*                           [win and py2k]
    requirements:                                                      [py2k]
      run_exports:                                                     [py2k]
        - {{ pin_subpackage("libboost_date_time", exact=True) }}       [py2k]
  - name: libboost_filesystem                                          [py2k]
    files:                                                             [py2k]
      - lib/libboost_filesystem*                           [not win and py2k]
      - Library\lib\\boost_filesystem*                          [win and py2k]
      - Library\lib\libboost_filesystem*                       [win and py2k]
      - Library\\bin\\boost_filesystem*                          [win and py2k]
    requirements:                                                      [py2k]
      run_exports:                                                     [py2k]
        - {{ pin_subpackage("libboost_filesystem", exact=True) }}      [py2k]
      run:                                                             [py2k]
        - {{ pin_subpackage("libboost_system", exact=True) }}          [py2k]
  - name: libboost_graph                                               [py2k]
    files:                                                             [py2k]
      - lib/libboost_graph*                                [not win and py2k]
      - Library\lib\\boost_graph*                               [win and py2k]
      - Library\lib\libboost_graph*                            [win and py2k]
      - Library\\bin\\boost_graph*                               [win and py2k]
    requirements:                                                      [py2k]
      run_exports:                                                     [py2k]
        - {{ pin_subpackage("libboost_graph", exact=True) }}           [py2k]
      run:                                                             [py2k]
        - {{ pin_subpackage("libboost_regex", exact=True) }}           [py2k]
        - icu 58.*                                           [linux and py2k]
  - name: libboost_iostreams                                           [py2k]
    files:                                                             [py2k]
      - lib/libboost_iostreams*                            [not win and py2k]
      - Library\lib\\boost_iostreams*                           [win and py2k]
      - Library\lib\libboost_iostreams*                        [win and py2k]
      - Library\\bin\\boost_iostreams*                           [win and py2k]
  - name: libboost_locale                                              [py2k]
    files:                                                             [py2k]
      - lib/libboost_locale*                               [not win and py2k]
      - Library\lib\\boost_locale*                              [win and py2k]
      - Library\lib\libboost_locale*                           [win and py2k]
      - Library\\bin\\boost_locale*                              [win and py2k]
    requirements:                                                      [py2k]
      run_exports:                                                     [py2k]
        - {{ pin_subpackage("libboost_locale", exact=True) }}          [py2k]
      run:                                                             [py2k]
        - {{ pin_subpackage("libboost_chrono", exact=True) }}          [py2k]
        - {{ pin_subpackage("libboost_thread", exact=True) }}          [py2k]
        - {{ pin_subpackage("libboost_system", exact=True) }}          [py2k]
        - icu 58.*                                           [linux and py2k]
  - name: libboost_log                                                 [py2k] 
    files:                                                             [py2k]
      - lib/libboost_log*                                  [not win and py2k]
      - Library\lib\\boost_log*                                 [win and py2k]
      - Library\lib\libboost_log*                              [win and py2k]
      - Library\\bin\\boost_log*                                 [win and py2k]
    requirements:                                                      [py2k]
      run_exports:                                                     [py2k]
        - {{ pin_subpackage("libboost_log", exact=True) }}             [py2k]
      run:                                                             [py2k]
        - {{ pin_subpackage("libboost_regex", exact=True) }}           [py2k]
        - {{ pin_subpackage("libboost_filesystem", exact=True) }}      [py2k]
        - {{ pin_subpackage("libboost_date_time", exact=True) }}       [py2k]
        - {{ pin_subpackage("libboost_thread", exact=True) }}          [py2k]
        - {{ pin_subpackage("libboost_chrono", exact=True) }}          [py2k]
        - {{ pin_subpackage("libboost_system", exact=True) }}          [py2k]
        - {{ pin_subpackage("libboost_atomic", exact=True) }}          [py2k]
        - icu 58.*                                           [linux and py2k]
  - name: libboost_math                                                [py2k]
    files:                                                             [py2k]
      - lib/libboost_math*                                 [not win and py2k]
      - Library\lib\\boost_math*                                [win and py2k]
      - Library\lib\libboost_math*                             [win and py2k]
      - Library\\bin\\boost_math*                                [win and py2k]
    requirements:                                                      [py2k]
      run_exports:                                                     [py2k]
        - {{ pin_subpackage("libboost_math", exact=True) }}[            py2k]
  - name: libboost_program_options                                     [py2k]
    files:                                                             [py2k]
      - lib/libboost_program_options*                      [not win and py2k]
      - Library\lib\\boost_program_options*                     [win and py2k]
      - Library\lib\libboost_program_options*                  [win and py2k]
      - Library\\bin\\boost_program_options*                     [win and py2k]
    requirements:                                                      [py2k]
      run_exports:                                                     [py2k]
        - {{ pin_subpackage("libboost_program_options", exact=True) }} [py2k]
  - name: libboost_python
    files:
      - lib/libboost_python*                                        [not win]
      - Library\lib\\boost_python*                                       [win]
      - Library\lib\libboost_python*                                    [win]
      - Library\\bin\\boost_python*                                       [win]
    requirements:
      run_exports:
        - {{ pin_subpackage("libboost_python", exact=True) }}
        - python
      run:
        - python
  - name: libboost_random                                              [py2k]
    files:                                                             [py2k]
      - lib/libboost_random*                               [not win and py2k]
      - Library\lib\\boost_random*                              [win and py2k]
      - Library\lib\libboost_random*                           [win and py2k]
      - Library\\bin\\boost_random*                              [win and py2k]
    requirements:                                                      [py2k]
      run_exports:                                                     [py2k]
        - {{ pin_subpackage("libboost_random", exact=True) }}          [py2k]
      run:                                                             [py2k]
        - {{ pin_subpackage("libboost_system", exact=True) }}          [py2k]
  - name: libboost_regex                                               [py2k]
    files:                                                             [py2k]
      - lib/libboost_regex*                                [not win and py2k]
      - Library\lib\\boost_regex*                               [win and py2k]
      - Library\lib\libboost_regex*                            [win and py2k]
      - Library\\bin\\boost_regex*                               [win and py2k]
    requirements:                                                      [py2k]
      run_exports:                                                     [py2k]
        - {{ pin_subpackage("libboost_regex", exact=True) }}           [py2k]
      run:                                                             [py2k]
        - icu 58.*                                           [linux and py2k]
  - name: libboost_serialization                                       [py2k]
    files:                                                             [py2k]
      - lib/libboost_serialization*                        [not win and py2k]
      - lib/libboost_wserialization*                       [not win and py2k]
      - Library\lib\\boost_serialization*                       [win and py2k]
      - Library\lib\libboost_serialization*                    [win and py2k]
      - Library\\bin\\boost_serialization*                       [win and py2k]
      - Library\lib\\boost_wserialization*                      [win and py2k]
      - Library\lib\libboost_wserialization*                   [win and py2k]
      - Library\\bin\\boost_wserialization*                      [win and py2k]
    requirements:                                                      [py2k]
      run_exports:                                                     [py2k]
        - {{ pin_subpackage("libboost_serialization", exact=True) }}   [py2k]
      run:                                                             [py2k]
        - icu 58.*                                           [linux and py2k]
  - name: libboost_signals                                             [py2k]
    files:                                                             [py2k]
      - lib/libboost_signals*                              [not win and py2k]
      - Library\lib\\boost_signals*                             [win and py2k]
      - Library\lib\libboost_signals*                          [win and py2k]
      - Library\\bin\\boost_signals*                             [win and py2k]
    requirements:                                                      [py2k]
      run_exports:                                                     [py2k]
        - {{ pin_subpackage("libboost_signals", exact=True) }}         [py2k]
  - name: libboost_system                                              [py2k]
    files:                                                             [py2k]
      - lib/libboost_system*                               [not win and py2k]
      - Library\lib\\boost_system*                              [win and py2k]
      - Library\lib\libboost_system*                           [win and py2k]
      - Library\\bin\\boost_system*                              [win and py2k]
    requirements:                                                      [py2k]
      run_exports:                                                     [py2k]
        - {{ pin_subpackage("libboost_system", exact=True) }}          [py2k]
  - name: libboost_test                                                [py2k]
    files:                                                             [py2k]
      - lib/libboost_unit_test_framework*                  [not win and py2k]
      - lib/libboost_prg_exec_monitor*                     [not win and py2k]
      - Library\lib\\boost_unit_test_framework*                 [win and py2k]
      - Library\lib\libboost_unit_test_framework*              [win and py2k]
      - Library\\bin\\boost_unit_test_framework*                 [win and py2k]
      - Library\lib\\boost_prg_exec_monitor*                    [win and py2k]
      - Library\lib\libboost_prg_exec_monitor*                 [win and py2k]
      - Library\\bin\\boost_prg_exec_monitor*                    [win and py2k]
    requirements:                                                      [py2k]
      run_exports:                                                     [py2k]
        - {{ pin_subpackage("libboost_test", exact=True) }}            [py2k]
      run:                                                             [py2k]
        - {{ pin_subpackage("libboost_timer", exact=True) }}           [py2k]
        - {{ pin_subpackage("libboost_system", exact=True) }}          [py2k]
        - {{ pin_subpackage("libboost_chrono", exact=True) }}          [py2k]
        - icu 58.*                                           [linux and py2k]
  - name: libboost_thread                                              [py2k]
    files:                                                             [py2k]
      - lib/libboost_thread*                               [not win and py2k]
      - Library\lib\\boost_thread*                              [win and py2k]
      - Library\lib\libboost_thread*                           [win and py2k]
      - Library\\bin\\boost_thread*                              [win and py2k]
    requirements:                                                      [py2k]
      run_exports:                                                     [py2k]
        - {{ pin_subpackage("libboost_thread", exact=True) }}          [py2k]
      run:                                                             [py2k]
        - {{ pin_subpackage("libboost_system", exact=True) }}          [py2k]
        - {{ pin_subpackage("libboost_chrono", exact=True) }}          [py2k]
        - {{ pin_subpackage("libboost_date_time", exact=True) }}       [py2k]
        - icu 58.*                                           [linux and py2k]
  - name: libboost_timer                                               [py2k]
    files:                                                             [py2k]
      - lib/libboost_timer*                                [not win and py2k]
      - Library\lib\\boost_timer*                               [win and py2k]
      - Library\lib\libboost_timer*                            [win and py2k]
      - Library\\bin\\boost_timer*                               [win and py2k]
    requirements:                                                      [py2k]
      run_exports:                                                     [py2k]
        - {{ pin_subpackage("libboost_timer", exact=True) }}           [py2k]
      run:                                                             [py2k]
        - {{ pin_subpackage("libboost_chrono", exact=True) }}          [py2k]
        - {{ pin_subpackage("libboost_system", exact=True) }}          [py2k]
  - name: libboost_type_erasure                                        [py2k]
    files:                                                             [py2k]
      - lib/libboost_type_erasure*                         [not win and py2k]
      - Library\lib\\boost_type_erasure*                        [win and py2k]
      - Library\lib\libboost_type_erasure*                     [win and py2k]
      - Library\\bin\\boost_type_erasure*                        [win and py2k]
    requirements:                                                      [py2k]
      run_exports:                                                     [py2k]
        - {{ pin_subpackage("libboost_type_erasure", exact=True) }}    [py2k]
      run:                                                             [py2k]
        - {{ pin_subpackage("libboost_thread", exact=True) }}          [py2k]
        - {{ pin_subpackage("libboost_chrono", exact=True) }}          [py2k]
        - {{ pin_subpackage("libboost_system", exact=True) }}          [py2k]
  - name: libboost_wave                                                [py2k]
    files:                                                             [py2k]
      - lib/libboost_wave*                                 [not win and py2k]
      - Library\lib\\boost_wave*                                [win and py2k]
      - Library\lib\libboost_wave*                             [win and py2k]
      - Library\\bin\\boost_wave*                                [win and py2k]
    requirements:                                                      [py2k]
      run_exports:                                                     [py2k]
        - {{ pin_subpackage("libboost_wave", exact=True) }}            [py2k]
      run:                                                             [py2k]
        - {{ pin_subpackage("libboost_filesystem", exact=True) }}      [py2k]
        - {{ pin_subpackage("libboost_thread", exact=True) }}          [py2k]
        - {{ pin_subpackage("libboost_date_time", exact=True) }}       [py2k]
        - {{ pin_subpackage("libboost_chrono", exact=True) }}          [py2k]
        - {{ pin_subpackage("libboost_system", exact=True) }}          [py2k]
""")

        filehandler.write('  - name: libboost\n')
        filehandler.write('    run:\n')
        for library in NON_HEADER_ONLY:
            filehandler.write('      - {{ pin_subpackage("libboost_' + library + '", exact=True) }}\n')

        if graph:
            for node in networkx.algorithms.topological_sort(graph):
                filehandler.write('  - name: ' + node + '\n')
                files = graph.nodes[node]['files']
                if len(files) > 0:
                    filehandler.write('    files:' + '\n')
                    for file in files:
                        filehandler.write('      - include/' + file + '         [not win and py2k]\n')
                        filehandler.write('      - Library\include\\' + file.replace('/', '\\') + ' [win and py2k]\n')
                run_exports = graph.nodes[node].get('run_exports', [])
                predecessors = list(graph.predecessors(node))
                if len(predecessors + run_exports) > 0:
                    filehandler.write('    requirements:' + '\n')
                    if len(run_exports) > 0:
                        filehandler.write('      run_exports:' + '\n')
                        for run_export in run_exports:
                            filehandler.write('        - {{ pin_subpackage("' + run_export + '", exact=True) }}\n')
                    if len(predecessors) > 0:
                        filehandler.write('      run:' + '\n')
                        for predecessor in predecessors:
                            filehandler.write('        - {{ pin_subpackage("' + predecessor + '", exact=True) }}\n')
        else:
            filehandler.write('  - name: libboost_core-dev\n')
            filehandler.write('    files:\n')
            filehandler.write('      - include/boost                                      [not win and py2k]\n')
            filehandler.write('      - Library\include\\boost                                  [win and py2k]\n')

write_meta()

subprocess.check_output('conda build . -c statiskit', shell=True)
subprocess.check_output('conda install libboost_core-dev --use-local -c statiskit -y', shell=True)

def create_graph(non_only_header=False):
    LIBS_DIR = Path('boost')
    LIBS_DIR /= 'libs'

    LIBS_DIRS =  [LIBS_DIR] + [directory for directory in LIBS_DIR.dirs() if (directory/'sublibs').exists()]
    graph = networkx.DiGraph()
    for lib_dir in LIBS_DIRS:
        for library in lib_dir.dirs():
            INCLUDE_DIR = library/'include'
            if INCLUDE_DIR.exists():
                libname = str(library.basename())
                graph.add_node('libboost_' + libname + '-dev',
                               files = [str(file.relpath(INCLUDE_DIR)) for file in (library/'include').walkfiles()],
                               run_exports = ['libboost_' + libname] * bool(libname in NON_HEADER_ONLY))
    for lib_dir in LIBS_DIRS:
        libname = str(lib_dir.basename())
        if libname == 'libs':
            libname = ''
        else:
            libname = '_' + libname
        libname = 'libboost' + libname + '-dev'
        if not libname in graph.nodes:
            graph.add_node(libname,
                           files = [],
                           run_exports = [])
        for sublibrary in lib_dir.dirs():
            INCLUDE_DIR = sublibrary/'include'
            if INCLUDE_DIR.exists():
                sublibname = str(sublibrary.basename())
                graph.add_edge('libboost_' + sublibname + '-dev', libname, capacity=0)
    if non_only_header:
        for node in graph.nodes.keys():
            if not node == 'libboost_core-dev':
                if len(graph.nodes[node]['run_exports']) == 0:
                    graph.nodes['libboost_core-dev']['files'].extend(graph.nodes[node]['files'])
                    graph.remove_node(node)
    return graph

graph = create_graph(non_only_header=True)

def add_edges(graph):
    inexisting = set()
    files = dict()
    for node in graph.nodes:
        files.update({file : node for file in graph.nodes[node]['files']})
    for node in graph.nodes:
        with NamedTemporaryFile(dir=os.environ['CONDA_PREFIX'] + '/include/boost', suffix='.hpp', delete=False) as filehandler:
            filehandler.write("\n".join("#include <" + file + ">" for file in graph.nodes[node]['files']))
        process = subprocess.Popen('bcp --scan --list --boost=$CONDA_PREFIX/include '  + filehandler.name, cwd=os.environ['CONDA_PREFIX'] + '/include/boost', stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        out, err = process.communicate()
        os.unlink(filehandler.name)
        edges = {edge : 0 for edge in graph.nodes if not edge == node}
        for file in out.split():
            filenode = files.get(file, None)
            if not filenode:
                inexisting.add(file)
            if filenode and not filenode == node:
                edges[filenode] = edges[filenode] + 1
        for edge, capacity in edges.iteritems():
            if capacity > 0:
                graph.add_edge(edge, node, capacity=capacity)
    return graph

graph = add_edges(graph)

def remove_edges(igraph):
    ograph = igraph.copy()
    for edge in ograph.edges.keys():
        ograph.remove_edge(*edge)
    for edge in sorted(igraph.edges, key=lambda edge: -igraph.edges[edge]['capacity']):
        ograph.add_edge(*edge)
        if not networkx.algorithms.is_directed_acyclic_graph(ograph):
            print edge
            ograph.remove_edge(*edge)
    return ograph

graph = remove_edges(graph)

def add_files(graph):
    for node in networkx.algorithms.topological_sort(graph):
        with NamedTemporaryFile(dir=os.environ['CONDA_PREFIX'] + '/include/boost', suffix='.hpp', delete=False) as filehandler:
            filehandler.write("\n".join("#include <" + file + ">" for file in graph.nodes[node]['files']))
        process = subprocess.Popen('bcp --scan --list --boost=$CONDA_PREFIX/include'  + filehandler.name, cwd=os.environ['CONDA_PREFIX'] + '/include/boost', stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        out, err = process.communicate()
        os.unlink(filehandler.name)
        files = set(graph.nodes[node]['files'])
        for ancestor in networkx.algorithms.ancestors(graph, node):
            files.update(graph.nodes[ancestor]['files'])
        for file in out.split():
            if not file in files and file.startswith('boost/'):
                graph.nodes[node]['files'].append(file)
    return graph

graph = add_files(graph)

write_meta(graph)
