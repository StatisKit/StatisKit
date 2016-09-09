##################################################################################
#                                                                                #
# PkgTk: Tool kit for Python packages                                            #
#                                                                                #
# Homepage: pkgtk.readthedocs.io                                                 #
#                                                                                #
# Copyright (c) 2016 Pierre Fernique                                             #
#                                                                                #
# This software is distributed under the CeCILL-C license. You should have       #
# received a copy of the legalcode along with this work. If not, see             #
# <http://www.cecill.info/licences/Licence_CeCILL-C_V1-en.html>.                 #
#                                                                                #
# File authors: Pierre Fernique <pfernique@gmail.com> (6)                        #
#                                                                                #
##################################################################################

import time
import string
import os

from .plugin import PluginManager
from .config import load_config, dump_config

def init_authors(repository, **kwargs):
    config = load_config(repository)
    authors = config.pop('authors', dict())
    if 'basename' not in authors or 'basename' in kwargs:
        basename = kwargs.pop('basename', '')
        if basename:
            authors['basename'] = basename
    if 'format' not in authors or 'format' in kwargs:
        format_string = kwargs.pop('format', '')
        if not format_string:
            format_string = '* {name} <{email}> ({score})'
        formatter = string.Formatter()
        for attr in formatter.parse(format_string):
            if attr[1] and not hasattr(Authors.Author, attr[1]):
                raise AttributeError('Authors.Author class has no attribute \'' + attr[1] + '\'')
        authors['format'] = format_string
    if 'plugin' not in authors or 'plugin' in kwargs:
        plugin = kwargs.pop('plugin', '')
        if not plugin:
            plugin = 'commit'
        if  plugin not in load_authors:
            raise ValueError('\'load_authors\' has no \'' + plugin + '\' plugin')
        authors['plugin'] = plugin
    config['authors'] = authors
    dump_config(repository, config)
    return config

class Authors(object):

    class Author(object):

        def __init__(self, name, oldest, latest, email, score):
            self._name = name
            self._oldest = oldest
            self._latest = latest
            self._email = email
            self._score = score

        @property
        def name(self):
            return self._name

        @property
        def oldest(self):
            return time.gmtime(self._oldest)

        @property
        def latest(self):
            return time.gmtime(self._latest)

        @property
        def email(self):
            return self._email

        @property
        def score(self):
            return self._score

    def __init__(self):
        self._oldests = dict()
        self._latests = dict()
        self._emails = dict()
        self._scores = dict()

    def __nonzero__(self):
        return len(self._emails) > 0

    def format(self, fmt):
        return ('\n'.join(fmt.format(name=author.name, email=author.email, score=author.score) for author in self.sorted)).strip()

    def add_commit(self, name, email, date, score=1):
        if name not in self._emails:
            self._emails[name] = email
        self._oldests[name] = min(self._oldests.pop(name, float("inf")), date)
        self._latests[name] = max(self._latests.pop(name, -float("inf")), date)
        self._scores[name] = self._scores.pop(name, 0) + score

    def finalize(self):
        emails = dict()
        for author in reversed(sorted(self.sorted, key=lambda author: author.latest)):
            if author.email in emails:
                self._oldests[emails[author.email]] = min(self._oldests[emails[author.email]], self._oldests[author.name])
                self._oldests.pop(author.name)
                self._latests[emails[author.email]] = max(self._latests[emails[author.email]], self._latests[author.name])
                self._latests.pop(author.name)
                self._scores[emails[author.email]] += self._scores[author.name]
                self._scores.pop(author.name)
                self._emails.pop(author.name)
            else:
                emails[author.email] = author.name
        self._emails = {name: email for email, name in emails.iteritems()}

    @property
    def sorted(self):
        return reversed(sorted([self.Author(name, self._oldests[name], self._latests[name], self._emails[name], self._scores[name])
                                for name in self._emails],
                               key=lambda author: author.score))

load_authors = PluginManager('pkgtk.load_authors',
        brief = "A plugin manager for loading authors from software repositories",
        details = """Authors are used to produce a `AUTHORS.*` file and in source\
                   code file license headers.

                   :Parameter:
                     `repository` (str) - The local path of the repository to consider.

                   :Optional Parameter:
                     `filepath` (str) - The local path of a file within the repository to consided.""")

def dump_authors(repository, config):
    authors = config['authors']
    load_authors.plugin = authors['plugin']
    if 'basename' in authors:
        with open(repository + os.sep + authors['basename'], 'w') as filehandler:
            filehandler.write(load_authors(repository).format(authors['format']))
