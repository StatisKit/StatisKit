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
      env['ANACONDA_CHANNELS'] = GetOption('anaconda-channels')
      def BuildConda(env, target, sources=[], exclude=[]):
        ANACONDA_CHANNELS = env.get('ANACONDA_CHANNELS')
        # ANACONDA_USERNAME = env.get('ANACONDA_USERNAME')
        channels = list(itertools.chain(*[['-c', channel] for channel in ANACONDA_CHANNELS]))
        targets = []
        SYSTEM = env['SYSTEM']
        if len(sources) == 0:
            sources = [env.Dir(".").srcnode()]
        if SYSTEM == 'win':
            conda = subprocess.check_output(['where', 'conda']).strip()
            recipes = [recipe for source in sources for recipe in path(source.abspath).walkdirs() if (recipe/'meta.yaml').exists() and (recipe/'bld.bat').exists()]
        else:
            conda = subprocess.check_output(['which', 'conda']).strip()
            recipes = [recipe for source in sources for recipe in path(source.abspath).walkdirs() if (recipe/'meta.yaml').exists() and (recipe/'build.sh').exists()]
        targets = []
        def compute_recipes(mode):
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

        for recipe in compute_recipes('build'):
            cmd = [conda, 'build', str(recipe)] + channels
            try:
                targets.append(env.Command(subprocess.check_output(cmd + ['--output']).strip(), recipe, " ".join(cmd)))
            except:
                pass
        if target == 'install':
            CONDA_ENVIRONMENT = path(conda).parent.parent
            target = env.Command(CONDA_ENVIRONMENT, compute_recipes('run'), conda + " install $SOURCES " + " ".join(channels))
            env.NoClean(target)
            for recipe in targets:
                env.Depends(target, recipe)
            return target
        else:
            return targets
        return targets

      env.AddMethod(BuildConda)

def exists(env):
    return 1
