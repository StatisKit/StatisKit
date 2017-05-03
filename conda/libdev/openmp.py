import os
from SCons.Defaults import Move, Delete

def generate(env):
    """Add Builders and construction variables to the Environment."""
    
    if not 'openmp' in env['TOOLS'][:-1]:
        env.Tool('system')
      if SYSTEM == 'win':
        env.AppendUnique(CCFLAGS=['/openmp'])
      else:
        env.PrependUnique(CFLAGS=["-fopenmp"])

def exists(env):
    return 1
