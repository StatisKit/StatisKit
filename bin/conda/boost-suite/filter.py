import argparse
import os
import sys
import pickle

if sys.version_info[0] == 2:
    PY2 = True
    PY3 = False
else:
    PY3 = True
    PY2 = False

def main(src):
    filtered = set()
    for root, dirs, files in os.walk(src):
        for file in files:
            filtered.add(os.path.join(root, file))
    return filtered

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--src", dest = 'src',
                                 help="Source directory to copy")
    parser.add_argument("--dst", dest = 'dst',
                                 help="Destination of the set pickle file")
    args = parser.parse_args()
    filtered = main(src = os.path.expandvars(args.src))
    if PY2:
        with open(os.path.expandvars(args.dst), "w") as filehandler:
            pickle.dump(filtered, filehandler)
    else:
        with open(os.path.expandvars(args.dst), "wb") as filehandler:
            pickle.dump(filtered, filehandler)