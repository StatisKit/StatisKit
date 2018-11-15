import os
import shutil
import re

SRC_DIR = os.environ['SRC_DIR']
if not "win" in os.environ["target_platform"]:
    SRC_DIR = os.path.join(SRC_DIR, 'Library')
    PREFIX = os.path.join(SRC_DIR, 'lib')
else:
    PREFIX = os.path.join(SRC_DIR, 'Library', 'lib')
BUILD_PREFIX = os.environ['BUILD_PREFIX']

for root, dirs, files in os.walk(PREFIX):
    root = os.path.abspath(root)
    for file in files:
        oldpath = os.path.join(root, file)
        if not os.path.islink(oldpath):
            if 'boost_python' in oldpath:
                newpath = oldpath.replace(SRC_DIR, BUILD_PREFIX, 1)
                dirpath = os.path.dirname(newpath)
                if not os.path.exists(dirpath):
                    os.makedirs(dirpath)
                shutil.move(oldpath, newpath)
                if "linux" in os.environ["target_platform"]:
                    sympath = re.sub('(.*)libboost_(.*).so(.*)', '\g<1>libboost_\g<2>.so', newpath)
                    if not sympath == newpath:
                        os.symlink(newpath, sympath)
                    sympath = re.sub('(.*)libboost_python(.*).so(.*)', '\g<1>libboost_python.so', newpath)
                    if not os.path.exists(sympath) and not sympath == newpath:
                        os.symlink(newpath, sympath)

if "win" in os.environ["target_platform"]:
    PREFIX = os.path.join(SRC_DIR, 'Library', 'bin')
    for root, dirs, files in os.walk(PREFIX):
        root = os.path.abspath(root)
        for file in files:
            oldpath = os.path.join(root, file)
            if not os.path.islink(oldpath):
                if 'boost_python' in oldpath:
                    newpath = oldpath.replace(SRC_DIR, BUILD_PREFIX, 1)
                    dirpath = os.path.dirname(newpath)
                    if not os.path.exists(dirpath):
                        os.makedirs(dirpath)
                    shutil.move(oldpath, newpath)