import yaml
import os
import networkx
from packaging.requirements import Requirement
import subprocess

subprocess.call(['anaconda', 'login'])

recipes = networkx.DiGraph()
for recipe in os.listdir('.'):
    if os.path.isdir(recipe) and os.path.exists(os.path.join(recipe, 'meta.yaml')):
        recipes.add_node(recipe)

for package in recipes.nodes():
    with open(os.path.join(package, 'meta.yaml'), 'r') as filehandler:
        meta = yaml.load(filehandler.read())
        requirements = meta.pop('requirements', {}).pop('build', [])
        for requirement in requirements:
            requirement = Requirement(requirement).name
            if requirement in recipes:
                recipes.add_edge(requirement, package)

recipes = networkx.topological_sort(recipes)
for recipe in recipes:
    subprocess.call(['conda', 'build', recipe, '-c', 'statiskit'])
    filename = subprocess.check_output(['conda', 'build', recipe, '--output']).strip()
    subprocess.call(['anaconda', 'upload', '--force', '--user', 'statiskit', filename])
