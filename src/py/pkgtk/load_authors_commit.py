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

import git
import os

from .vcs import get_vcs
from .authors import Authors

def load_authors(repository, filepath=''):
    authors = Authors()
    vcs = get_vcs(repository)
    if vcs == 'git':
        repository = git.Repo(repository)
        if filepath:
            filepath = os.path.relpath(os.path.abspath(filepath), repository.working_dir)
        for commit in repository.iter_commits(paths=filepath):
            author = commit.author
            authors.add_commit(author.name, author.email, commit.committed_date)
    authors.finalize()
    return authors
