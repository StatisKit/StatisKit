from path import Path
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

      AddOption('--conda-packages',
                dest = 'conda-packages',
                type = 'string',
                nargs = '+',
                action = 'store',
                help = 'Conda packages to build, install or upload',
                default = ['all'])
      env['CONDA_PACKAGES'] = GetOption('conda-packages')

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

    def list_packages(env, sources):
        SYSTEM = env['SYSTEM']
        sources = [Path(source.abspath).abspath() for source in sources]
        if SYSTEM == 'win':
            recipes = [source.abspath() for source in sources if (source/'meta.yaml').exists() and (source/'bld.bat').exists()]
        else:
            recipes = [source.abspath() for source in sources if (source/'meta.yaml').exists() and (source/'build.sh').exists()]
        packages = dict()
        for recipe in recipes:
            subprocess.check_output(['conda', 'render', recipe, '-f', os.path.join(recipe, 'meta.yaml.rendered')]).strip()
            with open(os.path.join(recipe, 'meta.yaml.rendered'), 'r') as filehandler:
                packages[yaml.load(filehandler)['package']['name']] = recipe
            os.unlink(os.path.join(recipe, 'meta.yaml.rendered'))
        return packages

    def CondaPackages(env, sources):
        condaenv = env.Clone()
        condaenv['ENV'].update(os.environ)
        CONDA_CHANNELS = condaenv['CONDA_CHANNELS']
        CONDA_PACKAGES = condaenv['CONDA_PACKAGES']
        targets = []
        packages = list_packages(condaenv, sources)
        if 'all' in CONDA_PACKAGES:
            CONDA_PACKAGES = [package for package in packages.iterkeys()] + [package for package in CONDA_PACKAGES if not package == 'all']
        for package, recipe in packages.iteritems():
            cmd = ['conda', 'render', recipe, '-f', os.path.join(recipe, 'meta.yaml.rendered')]
            subprocess.check_output(cmd).strip()
            with open(os.path.join(recipe, 'meta.yaml.rendered'), 'r') as filehandler:
                metadata = yaml.load(filehandler)
                if not metadata.get('build', {}).get('skip', False):
                    skip = False
                    cmd += ['--output']
                    target = Path(subprocess.check_output(cmd).strip())
                    target = condaenv.Command(target, recipe,
                                         "conda build " + recipe + " " + " ".join(CONDA_CHANNELS))
                    if package in CONDA_PACKAGES:
                        targets.extend(target)
                    for build in metadata.get('requirements', {}).get('build', []):
                        if build in packages:
                            archive = Path(subprocess.check_output(['conda',
                                                                    'build',
                                                                    packages[build],
                                                                    '--output']).strip())
                            condaenv.Depends(target, archive)
                else:
                    skip = True
            os.unlink(os.path.join(recipe, 'meta.yaml.rendered'))
            if not skip:
                depends = condaenv.Glob(os.path.join(recipe,'*'))
                condaenv.Depends(target, depends)
        return targets

    env.AddMethod(CondaPackages)

    def CondaEnvironment(env, sources):
        condaenv = env.Clone()
        condaenv['ENV'].update(os.environ)
        CONDA_CHANNELS = condaenv['CONDA_CHANNELS']
        CONDA_PACKAGES = condaenv['CONDA_PACKAGES']
        SYSTEM = condaenv['SYSTEM']
        if SYSTEM == 'win':
        	yes = 'echo y|'
        else:
        	yes = 'yes | '
        targets = []
        packages = list_packages(condaenv, sources)
        if 'all' in CONDA_PACKAGES:
            CONDA_PACKAGES = [package for package in packages.iterkeys()] + [package for package in CONDA_PACKAGES if not package == 'all']
        CONDA_PREFIX = condaenv['ENV']['CONDA_PREFIX']
        for package, recipe in packages.iteritems():
            cmd = ['conda', 'render', recipe, '-f', os.path.join(recipe, 'meta.yaml.rendered')]
            subprocess.check_output(cmd).strip()
            with open(os.path.join(recipe, 'meta.yaml.rendered'), 'r') as filehandler:
                metadata = yaml.load(filehandler)
                if not metadata.get('build', {}).get('skip', False):
                    cmd += ['--output']
                    archive = Path(subprocess.check_output(cmd).strip())
                    target = os.path.join(CONDA_PREFIX,
                                          'conda-meta',
                                          archive.name.replace('.tar.bz2', '.json', 1))
                    target = condaenv.Command(target, recipe,
                                         yes + 'conda' + " install -n " + os.path.basename(CONDA_PREFIX) + " " + package + " -y --use-local " + " ".join(CONDA_CHANNELS))
                    if os.path.exists(target[0].abspath):
                        with open(target[0].abspath, 'r') as filehandler:
                            for filename in json.loads("".join(filehandler.readlines())).get('files', []):
                                condaenv.Clean(target, os.path.join(CONDA_PREFIX, filename))
                    condaenv.Depends(target, archive)
                    if package in CONDA_PACKAGES:
                        targets.extend(target)
                    for run in metadata.get('requirements', {}).get('run', []):
                        if run in packages:
                            archive = Path(subprocess.check_output(['conda',
                                                                    'build',
                                                                    packages[run],
                                                                    '--output']).strip())
                            condaenv.Depends(target, os.path.join(CONDA_PREFIX,
                                                             'conda-meta',
                                                              archive.name.replace('.tar.bz2', '.json', 1)))
            os.unlink(os.path.join(recipe, 'meta.yaml.rendered'))
        return targets

    env.AddMethod(CondaEnvironment)

    def AnacondaUpload(env, sources):
        condaenv = env.Clone()
        condaenv['ENV'].update(os.environ)
        ANACONDA_CHANNEL = condaenv['ANACONDA_CHANNEL']
        ANACONDA_FORCE = condaenv['ANACONDA_FORCE']
        SYSTEM = condaenv['SYSTEM']
        CONDA_PACKAGES = condaenv['CONDA_PACKAGES']
        packages = list_packages(condaenv, sources)
        if 'all' in CONDA_PACKAGES:
            CONDA_PACKAGES = [package for package in packages.iterkeys()] + [package for package in CONDA_PACKAGES if not package == 'all']
        targets = []
        for package, recipe in packages.iteritems():
            if package in CONDA_PACKAGES:
                archive = Path(subprocess.check_output(['conda', 'build', recipe, '--output']).strip())
                targets.extend(condaenv.Command(archive + '.uploaded', archive, "anaconda upload " + archive.abspath() + " -u " * bool(ANACONDA_CHANNEL) + ANACONDA_CHANNEL + ' -f' * bool(ANACONDA_FORCE == 'yes')))
        return targets

    env.AddMethod(AnacondaUpload)

def exists(env):
    return 1