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
  git_url: https://github.com/boostorg/boost.git
  git_tag: boost-1.61.0

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
""")

        for node in networkx.algorithms.topological_sort(graph):
            if not node == 'libboost_core-dev' and len(graph.nodes[node]['files']) + len(graph.nodes[node].get('run_exports', [])) > 0:
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
                    if node == 'libboost_python-dev':
                        filehandler.write('      build:' + '\n')
                        filehandler.write('        - python\n')
                    if len(run_exports) > 0:
                        filehandler.write('      run_exports:' + '\n')
                        for run_export in run_exports:
                            filehandler.write('        - {{ pin_subpackage("' + run_export + '", exact=True) }}\n')
                    if len(predecessors) > 0:
                        filehandler.write('      run:' + '\n')
                        if node == 'libboost_python-dev':
                            filehandler.write('        - python\n')
                        for predecessor in predecessors:
                            if  len(graph.nodes[predecessor]['files']) + len(graph.nodes[predecessor].get('run_exports', [])) > 0:
                                filehandler.write('        - {{ pin_subpackage("' + predecessor + '", exact=True) }}\n')
                        if len(run_exports) > 0:
                            for run_export in run_exports:
                                filehandler.write('        - {{ pin_subpackage("' + run_export + '", exact=True) }}\n')


# subprocess.check_output('conda build . -c statiskit', shell=True)
# subprocess.call('conda remove libboost_core-dev -y', shell=True)
# subprocess.check_output('conda install libboost_core-dev --use-local -c statiskit -y', shell=True)

def create_graph(dispatch_files=True):
    LIBS_DIR = Path('boost')
    LIBS_DIR /= 'libs'

    LIBS_DIRS =  [LIBS_DIR] + [directory for directory in LIBS_DIR.dirs() if (directory/'sublibs').exists()]
    graph = networkx.DiGraph()
    for lib_dir in LIBS_DIRS:
        for library in lib_dir.dirs():
            INCLUDE_DIR = library/'include'
            if INCLUDE_DIR.exists():
                libname = str(library.basename())
                if dispatch_files:
                    files = [str(file.relpath(INCLUDE_DIR)) for file in (library/'include').walkfiles()]
                else:
                    files = []
                graph.add_node('libboost_' + libname + '-dev',
                               files = files,
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
    if not dispatch_files:
        for node in graph.nodes.keys():
            if not node == 'libboost_core-dev':
                graph.add_edge('libboost_core-dev', node)
    return graph

graph = create_graph(dispatch_files=False)
write_meta(graph)

# def add_edges(graph):
#     inexisting = set()
#     files = dict()
#     for node in graph.nodes:
#         files.update({file : node for file in graph.nodes[node]['files']})
#     for node in graph.nodes:
#         with NamedTemporaryFile(dir=os.environ['CONDA_PREFIX'] + '/include/boost', suffix='.hpp', delete=False) as filehandler:
#             filehandler.write("\n".join("#include <" + file + ">" for file in graph.nodes[node]['files']))
#         process = subprocess.Popen('bcp --scan --list --boost=$CONDA_PREFIX/include '  + filehandler.name, cwd=os.environ['CONDA_PREFIX'] + '/include/boost', stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
#         out, err = process.communicate()
#         os.unlink(filehandler.name)
#         edges = {edge : 0 for edge in graph.nodes if not edge == node}
#         for file in out.split():
#             filenode = files.get(file, None)
#             if not filenode:
#                 inexisting.add(file)
#             if filenode and not filenode == node:
#                 edges[filenode] = edges[filenode] + 1
#         for edge, capacity in edges.iteritems():
#             if capacity > 0:
#                 graph.add_edge(edge, node, capacity=capacity)
#     return graph

# graph = add_edges(graph)

# def remove_edges(igraph):
#     ograph = igraph.copy()
#     for edge in ograph.edges.keys():
#         ograph.remove_edge(*edge)
#     for edge in sorted(igraph.edges, key=lambda edge: -igraph.edges[edge]['capacity']):
#         ograph.add_edge(*edge)
#         if not networkx.algorithms.is_directed_acyclic_graph(ograph):
#             print edge
#             ograph.remove_edge(*edge)
#     return ograph

# graph = remove_edges(graph)

# def add_files(graph):
#     for node in networkx.algorithms.topological_sort(graph):
#         with NamedTemporaryFile(dir=os.environ['CONDA_PREFIX'] + '/include/boost', suffix='.hpp', delete=False) as filehandler:
#             filehandler.write("\n".join("#include <" + file + ">" for file in graph.nodes[node]['files']))
#         process = subprocess.Popen('bcp --scan --list --boost=$CONDA_PREFIX/include'  + filehandler.name, cwd=os.environ['CONDA_PREFIX'] + '/include/boost', stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
#         out, err = process.communicate()
#         os.unlink(filehandler.name)
#         files = set(graph.nodes[node]['files'])
#         for ancestor in networkx.algorithms.ancestors(graph, node):
#             files.update(graph.nodes[ancestor]['files'])
#         for file in out.split():
#             if not file in files and file.startswith('boost/'):
#                 graph.nodes[node]['files'].append(file)
#     return graph

# graph = add_files(graph)

# def remove_files(graph):
#     for node in graph.nodes:
#         directories = {}
#         for directory in {Path(os.environ['CONDA_PREFIX'] + '/include/' + file).parent for file in graph.nodes['files']}:
#             if all(str(item.relpath(os.environ['CONDA_PREFIX'] + '/include/')) in graph.nodes['files'] for item in directory.listdir()):
#                 directories.add(directory.relpath(os.environ['CONDA_PREFIX'] + '/include/'))
#     return graph

# graph = remove_files(graph)

# write_meta(graph)
