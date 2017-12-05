## Copyright [2017-2018] UMR MISTEA INRA, UMR LEPSE INRA,                ##
##                       UMR AGAP CIRAD, EPI Virtual Plants Inria        ##
## Copyright [2015-2016] UMR AGAP CIRAD, EPI Virtual Plants Inria        ##
##                                                                       ##
## This file is part of the StatisKit project. More information can be   ##
## found at                                                              ##
##                                                                       ##
##     http://statiskit.rtfd.io                                          ##
##                                                                       ##
## The Apache Software Foundation (ASF) licenses this file to you under  ##
## the Apache License, Version 2.0 (the "License"); you may not use this ##
## file except in compliance with the License. You should have received  ##
## a copy of the Apache License, Version 2.0 along with this file; see   ##
## the file LICENSE. If not, you may obtain a copy of the License at     ##
##                                                                       ##
##     http://www.apache.org/licenses/LICENSE-2.0                        ##
##                                                                       ##
## Unless required by applicable law or agreed to in writing, software   ##
## distributed under the License is distributed on an "AS IS" BASIS,     ##
## WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or       ##
## mplied. See the License for the specific language governing           ##
## permissions and limitations under the License.                        ##

import os
import platform
is_windows = any(platform.win32_ver())
PREFIX = os.environ['CONDA_PREFIX']
if is_windows:
    PREFIX = os.path.join(INCLUDE_DIR, 'Library')
INCLUDE_DIR = os.path.join(PREFIX, 'include', 'boost')

with open("SConstruct", "w") as filehandler:
    filehandler.write("""
env = Environment(tools = ['toolchain',
                           'cpp'])
env.AppendUnique(CPPDEFINES=["BOOST_GRAPH_USE_MPI"])
env.SharedLibrary("run_test", "run_test.cpp")
""")

with open("run_test.cpp", "w") as filehandler:
    for library in ["thread",
                    "chrono",
                    "program_options",
                    "filesystem",
                    "atomic",
                    "graph",
                    "math",
                    "random",
                    "container",
                    "coroutine",
                    "context",
                    "date_time",
                    "iostreams",
                    "locale",
                    "log",
                    "math",
                    "python",
                    "regex",
                    "serialization",
                    "signals",
                    "system",
                    "thread",
                    "timer",
                    "type_erasure",
                    "unit_test_frame_work",
                    "wave"]:
        if library == 'graph':
            break
        if os.path.exists(os.path.join(INCLUDE_DIR, library + '.h')):
            filehandler.write("#include <boost/" + library + ".h>\n")
            break
        if os.path.exists(os.path.join(INCLUDE_DIR, library + '.hpp')):
            filehandler.write("#include <boost/" + library + ".hpp>\n")
            break
        if os.path.exists(os.path.join(INCLUDE_DIR, library, 'all.hpp')):
            filehandler.write("#include <boost/" + library + "/all.hpp>\n")
            break
        if os.path.exists(os.path.join(INCLUDE_DIR, library)):
            for header in os.listdir(os.path.join(INCLUDE_DIR, library)):
                if os.path.isfile(os.path.join(INCLUDE_DIR, library, header)) and header.endswith('.hpp') and header not in ["leda_graph.hpp", 
                                                                                                                             "accounting.hpp",
                                                                                                                             "graph_test.hpp",
                                                                                                                             "use_mpi.hpp"]:
                    filehandler.write("#include <boost/" + library + "/" + header + ">\n")
            break
    filehandler.write("\nint main(void)\n{ return 0; }")

if library == 'python':
    with open("SConstruct", "a") as filehandler:
        filehandler.write("env.Tool('boost_python')")

with open("run_test.cpp", "r") as filehandler:
    if len(filehandler.readlines()) == 3 and not library == 'graph':
        raise Exception("no header included")

if os.system("scons --prefix=" + PREFIX):
    raise Exception("scons command failed")