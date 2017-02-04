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

      AddOption('--anaconda-channels',
                dest = 'anaconda-channels',
                type = 'string',
                nargs = '+',
                action = 'store',
                help = 'Channels to use for Conda build and install',
                default = ['statiskit', 'conda-forge'])
      env['ANACONDA_CHANNELS'] = list(itertools.chain(*[['-c', channel] for channel in GetOption('anaconda-channels')]))

    def list_recipes(env, sources, exclude):
        SYSTEM = env['SYSTEM']
        src_dir = path(env.Dir(".").srcnode().abspath)
        if len(sources) == 0:
            sources = [src_dir]
        else:
            sources = [path(source).abspath() for source in sources]
        if SYSTEM == 'win':
            conda = subprocess.check_output(['where', 'conda']).strip()
            recipes = [recipe for source in sources for recipe in source.dirs() if (recipe/'meta.yaml').exists() and (recipe/'bld.bat').exists()]
        else:
            conda = subprocess.check_output(['which', 'conda']).strip()
            recipes = [recipe for source in sources for recipe in source.dirs() if (recipe/'meta.yaml').exists() and (recipe/'build.sh').exists()]
        return conda, [recipe for recipe in recipes if recipe.relpath(src_dir) not in exclude]

    def order_recipes(mode, recipes):
        graph = networkx.DiGraph()
        for recipe in recipes:
            graph.add_node(str(recipe.name), path=recipe.abspath())
        for recipe in recipes:
            with open(recipe/'meta.yaml', 'r') as filehandler:
                rendered = ''.join(filehandler.readlines()).replace('{{ ', '$').replace(' }}', '')
                requirements = yaml.load(rendered).get('requirements', {}).get(mode, {})
            for requirement in requirements:
                requirement = requirement.split()[0]
                if requirement in graph:
                    graph.add_edge(requirement, str(recipe.name))
        return [graph.node[recipe]['path'] for recipe in networkx.topological_sort(graph)]

    def BuildConda(env, sources=[], exclude=[]):
        ANACONDA_CHANNELS =  env['ANACONDA_CHANNELS']
        conda, recipes = list_recipes(env, sources, exclude)
        targets = []
        for recipe in order_recipes('build', recipes):
            cmd = [conda, 'build', str(recipe)] + ANACONDA_CHANNELS
            try:
                targets.append(env.Command(subprocess.check_output(cmd + ['--output']).strip(), recipe, " ".join(cmd)))
            except:
                pass
        return targets

    env.AddMethod(BuildConda)

    def InstallConda(env, sources=[], exclude=[]):
        ANACONDA_CHANNELS = env['ANACONDA_CHANNELS']
        conda, recipes = list_recipes(env, sources, exclude)
        CONDA_ENVIRONMENT = path(conda).parent.parent
        targets = []
        for recipe in order_recipes('run', recipes):
            archive = path(subprocess.check_output([conda, 'build', str(recipe), '--output']).strip())
            target = os.path.join(CONDA_ENVIRONMENT,
                                  'conda-meta',
                                  archive.name.replace('.tar.bz2', '.json', 1))
            target = env.Command(target, recipe, conda + " install -n " + CONDA_ENVIRONMENT.name + " " + recipe.name + " -y --use-local " + " ".join(ANACONDA_CHANNELS))
            env.Depends(target, archive)
            targets.extend(target)
            target = path(targets[-1].abspath)
            if target.exists():
                with open(target, 'r') as filehandler:
                    for filename in json.loads("".join(filehandler.readlines())).get('files', []):
                        env.Clean(target, os.path.join(CONDA_ENVIRONMENT, filename))
        return targets

    env.AddMethod(InstallConda)

def exists(env):
    return 1
