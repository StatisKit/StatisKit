from path import path
import subprocess
import itertools
import yaml
from SCons.Script import AddOption, GetOption
import json
import os

def generate(env):
    """Add Builders and construction variables to the Environment."""
    if not 'conda' in env['TOOLS'][:-1]:
      env.Tool('system')

      AddOption('--conda-channels',
                dest = 'conda-channels',
                type = 'string',
                nargs = '+',
                action = 'store',
                help = 'Channels to use for Conda build and install',
                default = ['statiskit', 'conda-forge'])
      env['CONDA_CHANNELS'] = list(itertools.chain(*[['-c', channel] for channel in GetOption('conda-channels')]))

      AddOption('--anaconda-channel',
                dest = 'anaconda-channel',
                type = 'string',
                action = 'store',
                help = 'Anaconda channel to use for upload',
                default = '')
      env['ANACONDA_CHANNEL'] = GetOption('anaconda-channel')

      AddOption('--anaconda-force',
                dest = 'anaconda-force',
                type = 'choice',
                choices = ['yes', 'no'],
                action = 'store',
                help = 'Force upload to the Anaconda channel',
                default = 'no')
      env['ANACONDA_FORCE'] = GetOption('anaconda-force')

    env['ENV'].update(os.environ)

    def list_packages(env, sources):
        SYSTEM = env['SYSTEM']
        sources = [path(source.abspath).abspath() for source in sources]
        if SYSTEM == 'win':
            conda = subprocess.check_output(['where', 'conda.bat']).strip()
            recipes = [source.abspath() for source in sources if (source/'meta.yaml').exists() and (source/'bld.bat').exists()]
        else:
            conda = subprocess.check_output(['which', 'conda']).strip()
            recipes = [source.abspath() for source in sources if (source/'meta.yaml').exists() and (source/'build.sh').exists()]
        packages = dict()
        for recipe in recipes:
            subprocess.check_output([conda, 'render', recipe, '-f', os.path.join(recipe, 'meta.yaml.rendered')]).strip()
            with open(os.path.join(recipe, 'meta.yaml.rendered'), 'r') as filehandler:
                packages[yaml.load(filehandler)['package']['name']] = recipe
            os.unlink(os.path.join(recipe, 'meta.yaml.rendered'))
        return conda, packages

    def CondaPackages(env, sources):
        CONDA_CHANNELS =  env['CONDA_CHANNELS']
        targets = []
        conda, packages = list_packages(env, sources)
        CONDA_ENVIRONMENT = path(conda).parent.parent
        for recipe in packages.itervalues():
            cmd = [conda, 'render', recipe, '-f', os.path.join(recipe, 'meta.yaml.rendered')]
            subprocess.check_output(cmd).strip()
            with open(os.path.join(recipe, 'meta.yaml.rendered'), 'r') as filehandler:
                metadata = yaml.load(filehandler)
                if not metadata.get('build', {}).get('skip', False):
                    skip = False
                    cmd += ['--output']
                    target = path(subprocess.check_output(cmd).strip())
                    target = env.Command(target, recipe,
                                         conda + " build " + recipe + " " + " ".join(CONDA_CHANNELS))
                    targets.extend(target)
                    for build in metadata.get('requirements', {}).get('build', []):
                        if build in packages:
                            archive = path(subprocess.check_output([conda,
                                                                    'build',
                                                                    packages[build],
                                                                    '--output']).strip())
                            env.Depends(target, archive)
                else:
                    skip = True
            os.unlink(os.path.join(recipe, 'meta.yaml.rendered'))
            if not skip:
                depends = env.Glob(os.path.join(recipe,'*'))
                env.Depends(target, depends)
        return targets

    env.AddMethod(CondaPackages)

    def CondaEnvironment(env, sources):
        CONDA_CHANNELS = env['CONDA_CHANNELS']
        targets = []
        conda, packages = list_packages(env, sources)
        CONDA_ENVIRONMENT = path(conda).parent.parent
        for package, recipe in packages.iteritems():
            cmd = [conda, 'render', recipe, '-f', os.path.join(recipe, 'meta.yaml.rendered')]
            subprocess.check_output(cmd).strip()
            with open(os.path.join(recipe, 'meta.yaml.rendered'), 'r') as filehandler:
                metadata = yaml.load(filehandler)
                if not metadata.get('build', {}).get('skip', False):
                    cmd += ['--output']
                    archive = path(subprocess.check_output(cmd).strip())
                    target = os.path.join(CONDA_ENVIRONMENT,
                                          'conda-meta',
                                          archive.name.replace('.tar.bz2', '.json', 1))
                    target = env.Command(target, recipe,
                                         conda + " install -n " + CONDA_ENVIRONMENT.name + " " + package + " -y --use-local " + " ".join(CONDA_CHANNELS))
                    if os.path.exists(target.asbpath):
                        with open(target.abspath, 'r') as filehandler:
                            for filename in json.loads("".join(filehandler.readlines())).get('files', []):
                                env.Clean(target, os.path.join(CONDA_ENVIRONMENT, filename))
                    env.Depends(target, archive)
                    targets.extend(target)
                    for run in metadata.get('requirements', {}).get('run', []):
                        if run in packages:
                            archive = path(subprocess.check_output([conda,
                                                                    'build',
                                                                    packages[run],
                                                                    '--output']).strip())
                            env.Depends(target, os.path.join(CONDA_ENVIRONMENT,
                                                             'conda-meta',
                                                              archive.name.replace('.tar.bz2', '.json', 1)))
            os.unlink(os.path.join(recipe, 'meta.yaml.rendered'))
        return targets

    env.AddMethod(CondaEnvironment)

    def AnacondaUpload(env, sources):
        ANACONDA_CHANNEL = env['ANACONDA_CHANNEL']
        ANACONDA_FORCE = env['ANACONDA_FORCE']
        SYSTEM = env['SYSTEM']
        conda, packages = list_packages(env, sources)
        if SYSTEM == 'win':
            anaconda = subprocess.check_output(['where', 'anaconda.exe']).strip()
        else:
            anaconda = subprocess.check_output(['which', 'anaconda']).strip()
        targets = []
        for package, recipe in packages.iteritems():
            archive = path(subprocess.check_output([conda, 'build', recipe, '--output']).strip())
            targets.extend(env.Command(archive + '.uploaded', archive, anaconda + " upload " + archive.abspath() + " -u " * bool(ANACONDA_CHANNEL) + ANACONDA_CHANNEL + ' -f' * bool(ANACONDA_FORCE == 'yes')))
        return targets

    env.AddMethod(AnacondaUpload)

def exists(env):
    return 1
