import os
import shutil
from os.path import dirname, isdir, join


PREFIX = os.environ['PREFIX']
SCRIPTS = os.environ['SCRIPTS']
BITS = int(os.environ['ARCH'])

if BITS == 32:
    name = 'i686-w64-mingw32'
elif BITS == 64:
    name = 'x86_64-w64-mingw32'

mingw_dir = r'C:\MinGW\mingw%d' % BITS

dst_dir = join(PREFIX, 'MinGW', 'bin')
os.makedirs(dst_dir)
os.makedirs(SCRIPTS)
for fn in os.listdir(join(mingw_dir, 'bin')):
    if fn.endswith(('elfedit.exe', 'readelf.exe')):
        continue
    #assert fn.startswith(name + '-') and 
    #assert fn.endswith('.exe'), fn
    #sfn = fn[len(name) + 1:]
    if not fn.endswith('.exe'):
        continue
    sfn = fn[:]
    path = join(mingw_dir, 'bin', fn)
    shutil.copyfile(path, join(dst_dir, sfn))

    assert sfn.endswith('.exe')
    if sfn.startswith(name):
        continue
    noext = sfn[:-4]
    with open(join(SCRIPTS, noext + '.bat'), 'w') as fo:
        fo.write('@echo off\n'
                 '"%~f0\\..\\..\\MinGW\\bin\\' + noext + '.exe" %*\n')

for dn in [r'lib\gcc', 'libexec', name]:
    dir_path = join(mingw_dir, dn)
    for root, dirs, files in os.walk(dir_path):
        for fn in files:
            if fn in ['cc1obj.exe', 'cc1objplus', 'jc1.exe']:
                continue
            path = join(root, fn)
            filename = path[len(mingw_dir) + 1:]
            if filename.startswith(name) and filename.endswith('.dll'):
                shutil.copyfile(path, join(SCRIPTS, fn))
                continue

            if 'objc' in filename or (BITS == 64 and 'lib32' in filename):
                continue
            dst = join(PREFIX, 'MinGW', filename)
            if not isdir(dirname(dst)):
                os.makedirs(dirname(dst))
            shutil.copyfile(path, dst)