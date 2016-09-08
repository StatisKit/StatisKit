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

import os
import git
import github3
import parse
import re
import time

from getpass import getpass
from distutils.version import LooseVersion

from .vcs import get_vcs
from .about import About

def load_about(repository, config):
    global GITHUB_USERNAME, GITHUB_PASSWORD
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
        if any(field not in about for field in ['name', 'brief', 'homepage', 'version', 'authors', 'email']):
            session = github3.GitHub()
            if session.ratelimit_remaining == 0:
                delay = int(session.rate_limit()['rate']['reset'] - time.time()) + 1
                print 'Waiting for ' + str(delay) + 's'
                time.sleep(delay)
                session = github3.GitHub()
            owner = session.organization(result['owner'])
            if isinstance(owner, github3.null.NullObject):
                owner = session.user(result['owner'])
                owner.authors = [owner]
            else:
                owner.authors = list(owner.members())
            version = [tag.name for tag in git.Repo(repository).tags if  re.match('[A-Za-z]*(|-|_)[0-9]*\.[0-9]*(|\..*)', tag.name)]
            if version:
                version = max(version, key = lambda version: LooseVersion(version))
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

