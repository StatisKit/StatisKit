import argparse
import os
import sys
import shutil
import warnings
import pickle

if sys.version_info[0] == 2:
    PY2 = True
    PY3 = False
else:
    PY3 = True
    PY2 = False

def main(src, dst, filtered=set(), include=None, exclude=None):
    LINKS = dict()
    for root, dirs, files in os.walk(src):
        root = os.path.abspath(root)
        for file in files:
            oldpath = os.path.join(root, file)
            MOVE = oldpath not in filtered
            if MOVE and include:
                MOVE = include in oldpath
            if MOVE and exclude:
                MOVE = exclude not in oldpath
            if MOVE:
                if os.path.islink(oldpath):
                    LINKS[os.path.abspath(os.path.join(os.path.dirname(oldpath), os.readlink(oldpath))).replace(src, dst, 1)] = oldpath.replace(src, dst, 1)
                    os.unlink(oldpath)
                else:
                    newpath = oldpath.replace(src, dst, 1)
                    dirpath = os.path.dirname(newpath)
                    if not os.path.exists(dirpath):
                        os.makedirs(dirpath)
                    shutil.move(oldpath, newpath)
    changed = True
    if PY2:
        while changed and len(LINKS) > 0:
            changed = False
            for src, dst in LINKS.items():
                if os.path.exists(src):
                    if not os.path.exists(dst):
                        os.symlink(src, dst)
                    LINKS.pop(src)
                    changed = True
    else:
        while changed and len(LINKS) > 0:
            changed = False
            for src, dst in dict(LINKS).items():
                if os.path.exists(src):
                    if not os.path.exists(dst):
                        os.symlink(src, dst)
                    LINKS.pop(src)
                    changed = True
    if len(LINKS) > 0:
        warnings.warn("Files '" + "', ".join(key for key in LINKS.keys()) + "' have not been copied.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--src", dest = 'src',
                                 help="Source directory to copy")
    parser.add_argument("--dst", dest = 'dst',
                                 help="Destination directory to copy")
    parser.add_argument("--filtered", dest = 'filtered',
                                    default = None,
                                    help="File filter")
    parser.add_argument("--include", dest = "include",
                                     default = None,
                                     help = "Pattern moved files must contain")
    parser.add_argument("--exclude", dest = "exclude",
                                     default = None,
                                     help = "Pattern moved files must not contain")
    args = parser.parse_args()
    if args.filtered:
        if PY2:
            with open(args.filtered, 'r') as filehandler:
                filtered = pickle.load(filehandler)
        else:
            with open(args.filtered, 'rb') as filehandler:
                filtered = pickle.load(filehandler)
    else:
        filtered = set()
    main(src = os.path.expandvars(args.src),
         dst = os.path.expandvars(args.dst),
         filtered = filtered,
         include = args.include,
         exclude =args.exclude)