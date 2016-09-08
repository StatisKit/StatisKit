##################################################################################
#                                                                                #
# PkgTk: Tool kit for Python packages                                            #
#                                                                                #
# Homepage: http://pkgtk.readthedocs.io                                          #
#                                                                                #
# This software is distributed under the CeCILL-C license. You should have       #
# received a copy of the legalcode along with this work. If not, see             #
# <http://www.cecill.info/licences/Licence_CeCILL-C_V1-en.html>.                 #
#                                                                                #
# File authors: Pierre Fernique <pfernique@gmail.com> (4)                        #
#                                                                                #
##################################################################################

from .authors import load_authors

class Copyrights(object):

    class Copyright(object):

        def __init__(self, year, holders):
            self.oldest = year
            self.latest = year
            self.holders = holders

    def __init__(self):
        self._years = dict()

    def add_author(self, author):
        for year in range(author.oldest.tm_year, author.latest.tm_year+1):
            self._years[year] = self._years.pop(year, []) + [author.name]

    @property
    def sorted(self):
        copyrights = []
        years = sorted(self._years)
        while len(years) > 1:
            year = years.pop()
            copyrights.append(self.Copyright(year, self._years[year]))
            while len(years) > 0 and self._years[years[-1]] == copyrights[-1].holders:
                copyright.oldest = years.pop()
        return copyrights

def load_copyrights(repository, filepath, config):
    load_authors.plugin = config['authors']['plugin']
    authors = load_authors(repository, filepath,)
    copyrights = Copyrights()
    for author in authors.sorted:
        copyrights.add_author(author)
    return copyrights
