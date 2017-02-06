from path import path
import subprocess
import itertools
import yaml
import networkx
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

    def list_packages(env, sources):
        SYSTEM = env['SYSTEM']
        sources = [path(source.abspath).abspath() for source in sources]
        if SYSTEM == 'win':
            conda = subprocess.check_output(['where', 'conda']).strip()
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

    # def order_recipes(mode, recipes):
    #     graph = networkx.DiGraph()
    #     for recipe in recipes:
    #         graph.add_node(str(recipe.name), path=recipe.abspath())
    #     for recipe in recipes:
    #         with open(recipe/'meta.yaml', 'w') as filehandler:
    #             rendered = ''.join(filehandler.readlines()).replace('{{ ', '$').replace(' }}', '')
    #             requirements = yaml.load(rendered).get('requirements', {}).get(mode, {})
    #         for requirement in requirements:
    #             requirement = requirement.split()[0]
    #             if requirement in graph:
    #                 graph.add_edge(requirement, str(recipe.name))
    #     return [graph.node[recipe]['path'] for recipe in networkx.topological_sort(graph)]

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
            os.unlink(os.path.join(recipe, 'meta.yaml.rendered'))
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
        SYSTEM = env['SYSTEM']
        # clean = env.GetOption('clean')
        conda, packages = list_packages(env, sources)
        if SYSTEM == 'win':
            anaconda = subprocess.check_output(['where', 'anaconda']).strip()
        else:
            anaconda = subprocess.check_output(['which', 'anaconda']).strip()
        targets = []
        # if clean:
        #     for package, recipe in packages.iteritems():
        #         archive = path(subprocess.check_output([conda, 'build', recipe, '--output']).strip())
        #         subprocess.check_output([conda, 'render', recipe, '-f', os.path.join(recipe, 'meta.yaml.rendered')]).strip()
        #         with open(os.path.join(recipe, 'meta.yaml.rendered'), 'r') as filehandler:
        #             version = yaml.load(filehandler)['package']['version']
        #         os.unlink(os.path.join(recipe, 'meta.yaml.rendered'))
        #         if ANACONDA_CHANNEL:
        #             subprocess.call([anaconda, 'remove', '-f', '/'.join([ANACONDA_CHANNEL, package, version, archive.parent.name, archive.name])])
        # else:
        for package, recipe in packages.iteritems():
            archive = path(subprocess.check_output([conda, 'build', recipe, '--output']).strip())
            targets.extend(env.Command(archive + '.uploaded', archive, anaconda + " upload " + archive.abspath() + " -u " * bool(ANACONDA_CHANNEL) + ANACONDA_CHANNEL))
        return targets

    env.AddMethod(AnacondaUpload)

def exists(env):
    return 1
