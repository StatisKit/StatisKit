import os
import shutil

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