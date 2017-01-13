##################################################################################
#                                                                                #
# PkgTk: Tool kit for Python packages                                            #
#                                                                                #
# Homepage: pkg.readthedocs.io                                                 #
#                                                                                #
# Copyright (c) 2016 Pierre Fernique                                             #
#                                                                                #
# This software is distributed under the CeCILL-C license. You should have       #
# received a copy of the legalcode along with this work. If not, see             #
# <http://www.cecill.info/licences/Licence_CeCILL-C_V1-en.html>.                 #
#                                                                                #
# File authors: Pierre Fernique <pfernique@gmail.com> (16)                       #
#                                                                                #
##################################################################################

import git
import github3
import parse
import re
import time

from distutils.version import LooseVersion

from .vcs import get_vcs
from .about import About

def get_session(requests):
    session = github3.GitHub()
    if session.ratelimit_remaining < requests:
        raise Exception('Rate limit remaining is unsufficient, retry in ' + str(int(session.rate_limit()['rate']['reset'] - time.time()) + 1) + ' seconds')
    return session

def load_about(repository, config):
    vcs = get_vcs(repository)
    if vcs == 'git':
        about = config.get('about', dict())
        if 'remote' not in about:
            repo = git.Repo(repository)
            result = None
            swap = None
            for remote in repo.remotes:
                for url in remote.urls:
                    result = parse.parse('{protocol}://{host}/{owner}/{repository}.git', url)
                    if result and result['host'] == 'github.com':
                        break
                    else:
                        result = None
                if result:
                    if remote.name == 'upstream':
                        break
                    else:
                        swap = result
            if swap and not result:
                result = swap
        else:
            remote = about['remote']
            result = parse.parse('{protocol}://{host}/{owner}/{repository}.git', remote)
        if not result or not result['host'] == 'github.com':
            raise Exception("")
        about = config.get('about', dict())
        if any(field not in about for field in ['name', 'brief', 'homepage', 'version', 'authors', 'email']):
            session = get_session(2)
            owner = session.organization(result['owner'])
            if isinstance(owner, github3.null.NullObject):
                owner = session.user(result['owner'])
                owner.authors = [owner]
            else:
                owner.authors = [member.refresh() for member in owner.members()]
            session = get_session(len(owner.authors) * int('authors' not in about) + 1)
            version = [tag.name for tag in git.Repo(repository).tags if re.match('[A-Za-z]*(|-|_)[0-9]*\.[0-9]*(|\..*)', tag.name)]
            if version:
                version = max(version, key = LooseVersion)
            else:
                version = None
            repository = session.repository(result['owner'], result['repository'])
            about = About(name = about.get('name', repository.name),
                          brief = about.get('brief', repository.description),
                          homepage = about.get('homepage', repository.homepage),
                          version = about.get('version', version),
                          authors = about.get('authors', [author.name for author in owner.authors]),
                          email = about.get('email', owner.email))
        else:
            about = About(name = about['name'],
                          brief = about['brief'],
                          homepage = about['homepage'],
                          version = about['version'],
                          authors = about['authors'],
                          email = about['email'])
        return about
    else:
        raise Exception()

