from path import path
import subprocess
import itertools
import yaml
import networkx
from SCons.Script import AddOption, GetOption

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
        if len(sources) == 0:
            sources = [env.Dir(".").srcnode()]
        if SYSTEM == 'win':
            conda = subprocess.check_output(['where', 'conda']).strip()
            recipes = [recipe for source in sources for recipe in path(source.abspath).dirs() if (recipe/'meta.yaml').exists() and (recipe/'bld.bat').exists() and recipe not in exclude]
        else:
            conda = subprocess.check_output(['which', 'conda']).strip()
            recipes = [recipe for source in sources for recipe in path(source.abspath).dirs() if (recipe/'meta.yaml').exists() and (recipe/'build.sh').exists() and recipe not in exclude]
        return conda, recipes

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
        target = env.Command(CONDA_ENVIRONMENT, [recipe.name for recipe in order_recipes('run', recipes)], conda + " install $SOURCES " + " ".join(ANACONDA_CHANNELS))
        env.NoClean(target)
        for recipe in env.BuildConda(sources, exclude):
            env.Depends(target, recipe)
        return target

      env.AddMethod(InstallConda)

def exists(env):
    return 1
