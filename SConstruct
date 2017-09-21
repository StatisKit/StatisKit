# -*-python-*-

import os
from SCons.Errors import EnvironmentError

env = Environment()

try:
  SConscript(os.path.join('bin', 'conda', 'SConscript'), exports="env")
except Exception:
    raise

Default("install")