import os
import yaml
import subprocess
import networkx
import shutil
import re
import itertools

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

process = subprocess.Popen('git clone --recursive http://github.com/boostorg/boost',
                                           stdout=subprocess.PIPE,
                                           stderr=subprocess.PIPE,
                                           shell=True)
out, err = process.communicate()

process = subprocess.Popen('git -C boost checkout boost-1.61.0',
                           stdout=subprocess.PIPE,
                           stderr=subprocess.PIPE,
                           shell=True)
out, err = process.communicate()

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
  - name: libboost_atomic
    files:
      - lib/libboost_atomic*         [not win]
      - Library\lib\\boost_atomic*    [win]
      - Library\lib\libboost_atomic* [win]
      - Library\\bin\\boost_atomic*    [win]
    requirements:
      run_exports:
        - {{ pin_subpackage("libboost_atomic", exact=True) }}
  - name: libboost_chrono
    files:
      - lib/libboost_chrono*         [not win]
      - Library\lib\\boost_chrono*    [win]
      - Library\lib\libboost_chrono* [win]
      - Library\\bin\\boost_chrono*    [win]
    requirements:
      run:
        - {{ pin_subpackage("libboost_system", exact=True) }}
      run_exports:
        - {{ pin_subpackage("libboost_chrono", exact=True) }}
  - name: libboost_container
    files:
      - lib/libboost_container*         [not win]
      - Library\lib\\boost_container*    [win]
      - Library\lib\libboost_container* [win]
      - Library\\bin\\boost_container*    [win]
    requirements:
      run_exports:
        - {{ pin_subpackage("libboost_container", exact=True) }}
  - name: libboost_context
    files:
      - lib/libboost_context*         [not win]
      - Library\lib\\boost_context*    [win]
      - Library\lib\libboost_context* [win]
      - Library\\bin\\boost_context*    [win]
  - name: libboost_coroutine
    files:
      - lib/libboost_coroutine*         [not win]
      - Library\lib\\boost_coroutine*    [win]
      - Library\lib\libboost_coroutine* [win]
      - Library\\bin\\boost_coroutine*    [win]
    requirements:
      run_exports:
        - {{ pin_subpackage("libboost_coroutine", exact=True) }}
      run:
        - {{ pin_subpackage("libboost_system", exact=True) }}
        - {{ pin_subpackage("libboost_chrono", exact=True) }}
        - {{ pin_subpackage("libboost_thread", exact=True) }}
        - {{ pin_subpackage("libboost_context", exact=True) }}
  - name: libboost_date_time
    files:
      - lib/libboost_date_time*     [not win]
      - Library\lib\\boost_date_time*    [win]
      - Library\lib\libboost_date_time* [win]
      - Library\\bin\\boost_date_time*   [win]
    requirements:
      run_exports:
        - {{ pin_subpackage("libboost_date_time", exact=True) }}
  - name: libboost_filesystem
    files:
      - lib/libboost_filesystem*         [not win]
      - Library\lib\\boost_filesystem*    [win]
      - Library\lib\libboost_filesystem* [win]
      - Library\\bin\\boost_filesystem*    [win]
    requirements:
      run_exports:
        - {{ pin_subpackage("libboost_filesystem", exact=True) }}
      run:
        - {{ pin_subpackage("libboost_system", exact=True) }}
  - name: libboost_graph
    files:
      - lib/libboost_graph*         [not win]
      - Library\lib\\boost_graph*    [win]
      - Library\lib\libboost_graph* [win]
      - Library\\bin\\boost_graph*    [win]
    requirements:
      run_exports:
        - {{ pin_subpackage("libboost_graph", exact=True) }}
      run:
        - {{ pin_subpackage("libboost_regex", exact=True) }}
        - icu 58.*                  [linux]
  - name: libboost_iostreams
    files:
      - lib/libboost_iostreams*         [not win]
      - Library\lib\\boost_iostreams*    [win]
      - Library\lib\libboost_iostreams* [win]
      - Library\\bin\\boost_iostreams*    [win]
  - name: libboost_locale
    files:
      - lib/libboost_locale*         [not win]
      - Library\lib\\boost_locale*    [win]
      - Library\lib\libboost_locale* [win]
      - Library\\bin\\boost_locale*    [win]
    requirements:
      run_exports:
        - {{ pin_subpackage("libboost_locale", exact=True) }}
      run:
        - {{ pin_subpackage("libboost_chrono", exact=True) }}
        - {{ pin_subpackage("libboost_thread", exact=True) }}
        - {{ pin_subpackage("libboost_system", exact=True) }}
        - icu 58.*                  [linux]
  - name: libboost_log
    files:
      - lib/libboost_log*         [not win]
      - Library\lib\\boost_log*    [win]
      - Library\lib\libboost_log* [win]
      - Library\\bin\\boost_log*    [win]
    requirements:
      run_exports:
        - {{ pin_subpackage("libboost_log", exact=True) }}
      run:
        - {{ pin_subpackage("libboost_regex", exact=True) }}
        - {{ pin_subpackage("libboost_filesystem", exact=True) }}
        - {{ pin_subpackage("libboost_date_time", exact=True) }}
        - {{ pin_subpackage("libboost_thread", exact=True) }}
        - {{ pin_subpackage("libboost_chrono", exact=True) }}
        - {{ pin_subpackage("libboost_system", exact=True) }}
        - {{ pin_subpackage("libboost_atomic", exact=True) }}
        - icu 58.*                  [linux]
  - name: libboost_math
    files:
      - lib/libboost_math*         [not win]
      - Library\lib\\boost_math*    [win]
      - Library\lib\libboost_math* [win]
      - Library\\bin\\boost_math*    [win]
    requirements:
      run_exports:
        - {{ pin_subpackage("libboost_math", exact=True) }}
  - name: libboost_program_options
    files:
      - lib/libboost_program_options*          [not win]
      - Library\lib\\boost_program_options*     [win]
      - Library\lib\libboost_program_options*  [win]
      - Library\\bin\\boost_program_options*     [win]
    requirements:
      run_exports:
        - {{ pin_subpackage("libboost_program_options", exact=True) }}
  - name: libboost_python
    files:
      - lib/libboost_python*         [not win]
      - Library\lib\\boost_python*    [win]
      - Library\lib\libboost_python* [win]
      - Library\\bin\\boost_python*    [win]
    requirements:
      run_exports:
        - {{ pin_subpackage("libboost_python", exact=True) }}
        - python
      run:
        - python
  - name: libboost_random
    files:
      - lib/libboost_random*         [not win]
      - Library\lib\\boost_random*    [win]
      - Library\lib\libboost_random* [win]
      - Library\\bin\\boost_random*    [win]
    requirements:
      run_exports:
        - {{ pin_subpackage("libboost_random", exact=True) }}
      run:
        - {{ pin_subpackage("libboost_system", exact=True) }}
  - name: libboost_regex
    files:
      - lib/libboost_regex*         [not win]
      - Library\lib\\boost_regex*    [win]
      - Library\lib\libboost_regex* [win]
      - Library\\bin\\boost_regex*    [win]
    requirements:
      run_exports:
        - {{ pin_subpackage("libboost_regex", exact=True) }}
      run:
        - icu 58.*                  [linux]
  - name: libboost_serialization
    files:
      - lib/libboost_serialization*          [not win]
      - lib/libboost_wserialization*         [not win]
      - Library\lib\\boost_serialization*    [win]
      - Library\lib\libboost_serialization*  [win]
      - Library\\bin\\boost_serialization*     [win]
      - Library\lib\\boost_wserialization*    [win]
      - Library\lib\libboost_wserialization* [win]
      - Library\\bin\\boost_wserialization*    [win]
    requirements:
      run_exports:
        - {{ pin_subpackage("libboost_serialization", exact=True) }}
      run:
        - icu 58.*                  [linux]
  - name: libboost_signals
    files:
      - lib/libboost_signals*         [not win]
      - Library\lib\\boost_signals*    [win]
      - Library\lib\libboost_signals* [win]
      - Library\\bin\\boost_signals*    [win]
    requirements:
      run_exports:
        - {{ pin_subpackage("libboost_signals", exact=True) }}
  - name: libboost_system
    files:
      - lib/libboost_system*         [not win]
      - Library\lib\\boost_system*    [win]
      - Library\lib\libboost_system* [win]
      - Library\\bin\\boost_system*    [win]
    requirements:
      run_exports:
        - {{ pin_subpackage("libboost_system", exact=True) }}
  - name: libboost_test
    files:
      - lib/libboost_unit_test_framework*          [not win]
      - lib/libboost_prg_exec_monitor*             [not win]
      - Library\lib\\boost_unit_test_framework*     [win]
      - Library\lib\libboost_unit_test_framework*  [win]
      - Library\\bin\\boost_unit_test_framework*     [win]
      - Library\lib\\boost_prg_exec_monitor*        [win]
      - Library\lib\libboost_prg_exec_monitor*     [win]
      - Library\\bin\\boost_prg_exec_monitor*        [win]
    requirements:
      run_exports:
        - {{ pin_subpackage("libboost_test", exact=True) }}
      run:
        - {{ pin_subpackage("libboost_timer", exact=True) }}
        - {{ pin_subpackage("libboost_system", exact=True) }}
        - {{ pin_subpackage("libboost_chrono", exact=True) }}
        - icu 58.*                  [linux]
  - name: libboost_thread
    files:
      - lib/libboost_thread*         [not win]
      - Library\lib\\boost_thread*    [win]
      - Library\lib\libboost_thread* [win]
      - Library\\bin\\boost_thread*    [win]
    requirements:
      run_exports:
        - {{ pin_subpackage("libboost_thread", exact=True) }}
      run:
        - {{ pin_subpackage("libboost_system", exact=True) }}
        - {{ pin_subpackage("libboost_chrono", exact=True) }}
        - {{ pin_subpackage("libboost_date_time", exact=True) }}
        - icu 58.*                  [linux]
  - name: libboost_timer
    files:
      - lib/libboost_timer*         [not win]
      - Library\lib\\boost_timer*    [win]
      - Library\lib\libboost_timer* [win]
      - Library\\bin\\boost_timer*    [win]
    requirements:
      run_exports:
        - {{ pin_subpackage("libboost_timer", exact=True) }}
      run:
        - {{ pin_subpackage("libboost_chrono", exact=True) }}
        - {{ pin_subpackage("libboost_system", exact=True) }}
  - name: libboost_type_erasure
    files:
      - lib/libboost_type_erasure*         [not win]
      - Library\lib\\boost_type_erasure*    [win]
      - Library\lib\libboost_type_erasure* [win]
      - Library\\bin\\boost_type_erasure*    [win]
    requirements:
      run_exports:
        - {{ pin_subpackage("libboost_type_erasure", exact=True) }}
      run:
        - {{ pin_subpackage("libboost_thread", exact=True) }}
        - {{ pin_subpackage("libboost_chrono", exact=True) }}
        - {{ pin_subpackage("libboost_system", exact=True) }}
  - name: libboost_wave
    files:
      - lib/libboost_wave*         [not win]
      - Library\lib\\boost_wave*    [win]
      - Library\lib\libboost_wave* [win]
      - Library\\bin\\boost_wave*    [win]
    requirements:
      run_exports:
        - {{ pin_subpackage("libboost_wave", exact=True) }}
      run:
        - {{ pin_subpackage("libboost_filesystem", exact=True) }}
        - {{ pin_subpackage("libboost_thread", exact=True) }}
        - {{ pin_subpackage("libboost_date_time", exact=True) }}
        - {{ pin_subpackage("libboost_chrono", exact=True) }}
        - {{ pin_subpackage("libboost_system", exact=True) }}
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
                        filehandler.write('      - include/' + file + '         [not win]\n')
                        filehandler.write('      - Library\include\\' + file.replace('/', '\\') + ' [win]\n')
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
            filehandler.write('      - include/boost         [not win]\n')
            filehandler.write('      - Library\include\\boost [win]\n')

write_meta()

subprocess.check_output('conda build . -c statiskit', shell=True)
subprocess.check_output('conda install libboost_core-dev --use-local -c statiskit -y', shell=True)

def create_graph():
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
                               include_dir = INCLUDE_DIR,
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
                           include_dir = None,
                           run_exports = [])
        for sublibrary in lib_dir.dirs():
            INCLUDE_DIR = sublibrary/'include'
            if INCLUDE_DIR.exists():
                sublibname = str(sublibrary.basename())
                graph.add_edge('libboost_' + sublibname + '-dev', libname, capacity=0)
    return graph

graph = create_graph()

def add_edges(graph):
    inexisting = set()
    files = dict()
    for node in graph.nodes:
        files.update({file : node for file in graph.nodes[node]['files']})
    for node in graph.nodes:
        process = subprocess.Popen('bcp ' + ' '.join(file[6:] for file in graph.nodes[node]['files']) + ' --list --boost=$CONDA_PREFIX/include', cwd=os.environ['CONDA_PREFIX'] + '/include/boost', stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        out, err = process.communicate()
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
    ograph = create_graph()
    for edge in sorted(igraph.edges, key=lambda edge: igraph.edges[edge]['capacity']):
        ograph.add_edge(*edge)
        if not networkx.algorithms.is_directed_acyclic_graph(ograph):
            print edge
            ograph.remove_edge(*edge)
    return ograph

graph = remove_edges(graph)

def add_files(graph):
    for node in networkx.algorithms.topological_sort(graph):
        process = subprocess.Popen('bcp ' + ' '.join(file[6:] for file in graph.nodes[node]['files']) + ' --list --boost=$CONDA_PREFIX/include', cwd=os.environ['CONDA_PREFIX'] + '/include/boost', stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        out, err = process.communicate()
        files = set(graph.nodes[node]['files'])
        for ancestor in networkx.algorithms.ancestors(graph, node):
            files.update(graph.nodes[ancestor]['files'])
        for file in out.split():
            if not file in files and file.startswith('boost/'):
                graph.nodes[node]['files'].append(file)
    return graph

graph = add_files(graph)

write_meta(graph)
