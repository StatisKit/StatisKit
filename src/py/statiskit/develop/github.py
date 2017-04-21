from github3 import login
from github3.orgs import Organization

gh = login('sigmavirus24', password='<password>')


class GitHubSession(object):

    def __init__(self, username, password, two_factor_callback=None):
        self._username = username
        self._password = password
        self._session = login(username, password, token=None, two_factor_callback)

    def _travis_token(self):
        

    def create_repository(self, name, description, organization='StatisKit'):
        if not isinstance(name, basestring):
            raise TypeError('\'name\' parameter')
        if ' ' in name:
            raise ValueError('\'name\' parameter contains spaces')
        organization = Organization(organization, self._session)
        organization.create_repo(name, , description=description,
                                         homepage='http://statiskit.readthedocs.io/projects/' + name.lower(),
                                         private=False,
                                         has_issues=True,
                                         has_wiki=False,
                                         has_downloads=True,
                                         auto_init=False)
