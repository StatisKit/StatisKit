##################################################################################
#                                                                                #
# PkgTk: Toolkit for packaging                                                   #
#                                                                                #
# Homepage: pkgtk.readthedocs.io                                                 #
#                                                                                #
# This software is distributed under the CeCILL-C license. You should have       #
# received a copy of the legalcode along with this work. If not, see             #
# <http://www.cecill.info/licences/Licence_CeCILL-C_V1-en.html>.                 #
#                                                                                #
# File authors: Pierre Fernique <pfernique@gmail.com> (2)                        #
#                                                                                #
##################################################################################

import git
import github3
import parse

from .vcs import get_vcs
from .about import About

def load_about(repository, config):
    vcs = get_vcs(repository)
    if vcs == 'git':
        about = config.get('about', dict())
        if 'remote' not in about:
            repo = git.Repo(repository)
            result = None
            for remote in repo.remotes:
                for url in remote.urls:
                    result = parse.parse('{protocol}://{host}/{owner}/{repository}.git', url)
                    if result and result['host'] == 'github.com':
                        break
                    else:
                        result = None
                if result:
                    break
        else:
            remote = about['remote']
            result = parse.parse('{protocol}://{host}/{owner}/{repository}.git', remote)
        if not result or not result['host'] == 'github.com':
            raise Exception("")
        about = config.get('about', dict())
        if any(field not in about for field in ['name', 'brief', 'homepage']):
            session = github3.GitHub()
            repository = session.repository(result['owner'], result['repository'])
            about = About(name = about.get('name', repository.name),
                          brief = about.get('brief', repository.description),
                          homepage = about.get('homepage', repository.homepage))
        else:
            about = About(name = about['name'],
                          brief = about['brief'],
                          homepage = about['homepage'])
        return about
    else:
        raise Exception()

