import os
import shutil
from path import Path

if "win" in os.environ["target_platform"]:
    PREFIX = os.path.join(os.environ['SRC_DIR'], 'Library', 'include')
    BUILD_PREFIX = os.path.join(os.environ['BUILD_PREFIX'], 'Library', 'include')
else:
    PREFIX = os.path.join(os.environ['SRC_DIR'], 'prefix', 'include')
    BUILD_PREFIX = os.path.join(os.environ['BUILD_PREFIX'], 'include')

for oldpath in Path(PREFIX).walkfiles():
    if PREFIX in oldpath:
        newpath = oldpath.replace(PREFIX, BUILD_PREFIX, 1)
        dirpath = os.path.dirname(newpath)
        if not os.path.exists(dirpath):
            os.makedirs(dirpath)
        shutil.move(oldpath, newpath)