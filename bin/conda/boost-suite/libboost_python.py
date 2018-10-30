import os
import shutil
from path import Path

if "win" in os.environ["target_platform"]:
    PREFIX = os.path.join(os.environ['SRC_DIR'], 'Library', 'lib')
    BUILD_PREFIX = os.path.join(os.environ['BUILD_PREFIX'], 'Library', 'lib')
else:
    PREFIX = os.path.join(os.environ['SRC_DIR'], 'prefix', 'lib')
    BUILD_PREFIX = os.path.join(os.environ['BUILD_PREFIX'], 'lib')

for oldpath in Path(PREFIX).walkfiles():
    if PREFIX in oldpath and 'boost_python' in oldpath:
        newpath = oldpath.replace(PREFIX, BUILD_PREFIX, 1)
        dirpath = os.path.dirname(newpath)
        if not os.path.exists(dirpath):
            os.makedirs(dirpath)
        shutil.move(oldpath, newpath)

if "win" in os.environ["target_platform"]:
    PREFIX = os.path.join(os.environ['SRC_DIR'], 'Library', 'bin')
    BUILD_PREFIX = os.path.join(os.environ['BUILD_PREFIX'], 'Library', 'bin')

    for oldpath in Path(PREFIX).walkfiles():
        if PREFIX in oldpath and 'boost_python' in oldpath:
            newpath = oldpath.replace(PREFIX, BUILD_PREFIX, 1)
            dirpath = os.path.dirname(newpath)
            if not os.path.exists(dirpath):
                os.makedirs(dirpath)
            shutil.move(oldpath, newpath)