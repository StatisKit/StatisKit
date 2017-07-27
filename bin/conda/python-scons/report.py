import os
from SCons.Builder import Builder
from SCons.Action import Action
from hashlib import md5

def generate(env):
    """Add Builders and construction variables to the Environment."""

    if not 'autowig' in env['TOOLS'][:-1]:

        def coverage_builder(target, source, env):
            with open(source[0], 'r') as filehandler:
                line = filehandler.readline()
            line = 'coverage = ' + line[line.find('!', 2) + 1:] + '\ncoverage = coverage["lines"]'
            exec(line, locals())

            COVERAGE_SRC_DIRS = covenv['COVERAGE_SRC_DIRS']
            COVERAGE_TGT_DIRS = covenv['COVERAGE_TGT_DIRS']

            table = []
            for filepath in coverage:
                for tgt_dir in COVERAGE_TGT_DIRS:
                    if filepath.startswith(tgt_dir):
                        for src_dir in COVERAGE_SRC_DIRS:
                            report = ""
                            srcfilepath = src_dir + filepath[len(tgt_dir):]
                            if os.path.exists(srcfilepath):
                                srclabel = srcfilepath.replace('.', '-').replace('_', '-').replace(os.sep, '-').strip('-')
                                report += ".. _" + srclabel + ':\n'
                                report += "\nCoverage of the :file:`" + srcfilepath + "` source file\n"
                                report += "####################################" + "#" * len(srcfilepath)
                                report += "\n\n.. literalinclude:: " + os.path.relpath(srcfilepath, os.path.dirname(target[1].abspath))
                                report += "\n   :emphasize-lines: " + ", ".join(str(line) for line in coverage[filepath])
                                report += "\n   :linenos:\n"
                                with open(srcfilepath, 'r') as filehandler:
                                    lines  = filehandler.readlines()
                                    relevant = 0
                                    if filepath.endswith('.py'):
                                        rstfilepath = srcfilepath.replace('.py', '.rst')
                                        comment = False
                                        for line in lines:
                                            line = line.strip()
                                            if comment:
                                                comment = not line.endswith('"""')
                                            elif line.startswith('"""'):
                                                comment = not line.endswith('"""')
                                            elif line and not line.startswith('#'):
                                                relevant += 1
                                    lines = len(lines)
                                    covered = len(coverage[filepath])
                                    missed = relevant - covered
                                table.append([int(covered/float(relevant) * 100), ":ref:`" + srcfilepath + " <" + srclabel + ">`", lines, relevant, covered, missed])
                                coverage[filepath] = report
                                break
                        break

            covered = 0
            missed = 0
            for row in table:
                covered += row[-2]
                missed += row[-1]
            total = int(covered/float(covered + missed) * 100)
            if total < covenv['COVERAGE_RED']:
                color = "red"
            elif total < covenv['COVERAGE_ORANGE']:
                color = "orange"
            elif total < covenv['COVERAGE_YELLOW']:
                color = "yellow"
            elif total < covenv['COVERAGE_YELLOWGREEN']:
                color = "yellowgreen"
            elif total < covenv['COVERAGE_GREEN']:
                color = "green"
            else:
                color = "brightgreen"

            with open(target[0].abspath, 'w') as filehandler:
                filehandler.writelines([".. |COVERAGE| image:: https://img.shields.io/badge/coverage-" + str(total) + "%-" + color + ".svg\n",
                                        "              :target: " + target[1].rel_path(target[0])+ "\n",
                                        "              :alt: Coverage\n"])

            with open(target[1].abspath, 'w') as filehandler:
                table = sorted(table, key= lambda row: row[0])
                rows = [[str(row[0]) + "%"] + [str(column) for column in row[1:]] for row in table[1:]]
                rows = [["Coverage", "File", "Lines", "Excluded", "Covered", "Missed"]] + rows
                columns = zip(*rows)
                maxima = [max(max(*[len(row) for row in column]), 3) + 2 for column in columns]
                string = []
                for index, row in enumerate(rows):
                    string.append("+" + "-+".join(['-' * maximum for maximum in maxima]) + "--+\n")
                    string.append("| " + '| '.join(('{:<' + str(maximum) + '}').format(row[index]) for index, maximum in enumerate(maxima)) + " |\n")
                string.append("+" + "-+".join(['-' * maximum for maximum in maxima]) + "--+\n")
                string[2] = "+" + "=+".join(['=' * maximum for maximum in maxima]) + "==+\n"
                filehandler.writelines(["Coverage report\n",
                                        "###############\n\n"])
                filehandler.writelines(string)

            for filepath in coverage:
                with open(os.path.join(target[2].abspath, md5(filepath).hexdigest() + '.rst'), 'w') as filehandler:
                    filehandler.write(coverage[filepath])

            return None

        def CoverageReport(env, badge, report, annotate, sources, srcdirs=[], tgtdirs=[], red=75, orange=80, yellow=85, yellowgreen=90, green=95):

            covenv = env.Clone()
            covenv['BUILDERS']['_CoverageReport'] = Builder(action = Action(coverage_builder, 'coverage: Generating report ...'))
            covenv['COVERAGE_SRC_DIRS'] = srcdirs
            covenv['COVERAGE_TGT_DIRS'] = tgtdirs
            covenv['COVERAGE_RED'] = red
            covenv['COVERAGE_ORANGE'] = orange
            covenv['COVERAGE_YELLOW'] = yellow
            covenv['COVERAGE_YELLOWGREEN'] = yellowgreen
            covenv['COVERAGE_GREEN'] = green

            covenv._CoverageReport([covenv.File(badge), covenv.File(report), covenv.Dir(annotate)], sources)

            return targets

        env.AddMethod(BoostPythonWIG)

def exists(env):
    return 1