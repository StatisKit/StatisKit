import os
import yaml
import subprocess

with open('meta.yaml', 'r') as filehandler:
    META = yaml.load(filehandler)

with open('libraries.txt', 'r') as filehandler:
    libraries = [library.strip() for library in filehandler.readlines()]

libraries.append('lexical_cast')
OUTPUTS = {output['name'] : output for output in META.pop('outputs')}
TEST = META.pop('test')

with open('meta.yaml', 'w') as filehandler:
    filehandler.write(yaml.dump(META, default_flow_style=False))

try:
    result = subprocess.check_output(['conda', 'build', '.', '-c', 'statiskit'])
    result = subprocess.check_output(['conda', 'install', META['package']['name'], '--use-local', '-c', 'statiskit', '-y'])
except Exception as error:
    META['outputs'] = OUTPUTS.values()
    META['test'] = TEST
    with open('meta.yaml', 'w') as filehandler:
        filehandler.write(yaml.dump(META, default_flow_style=False))
    raise error
else:
    META['outputs'] = OUTPUTS.values()
    META['test'] = TEST
    with open('meta.yaml', 'w') as filehandler:
        filehandler.write(yaml.dump(META, default_flow_style=False))

INCLUDE_DIR = os.path.join(os.environ['CONDA_PREFIX'], 'include', 'boost')
for library in libraries:
    if not os.path.exists(os.path.join(INCLUDE_DIR, library)) and not library in ['any', 'array', 'callable_traits', 'conversion', 'crc', 'foreach', 'interval']:
        raise Exception("'" + library + "' has not include folder")
    print library+':'
    for dependency in libraries:
        if not dependency == library:
            process = subprocess.Popen('grep -r "boost/' + dependency + '" ' + os.path.join(os.environ['CONDA_PREFIX'], 'include', 'boost', library),
                                       stdout=subprocess.PIPE,
                                       stderr=subprocess.PIPE,
                                       shell=True)
            out, err = process.communicate()
            if out:
                print '\t' + dependency
                # OUTPUTS['lib' + library + '-dev']['requirements']['run'] = '"{{ pin_subpackage(\'\'libboost' + dependency + '_dev\'\', exact=True) }}"'
