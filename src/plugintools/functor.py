import pkg_resources

class PluginFunctorDescriptor(object):
    """A plugin plugin manager descriptor that returns and sets plugin_manager implementations
    """

    def __get__(self, obj, objtype):
        plugin = obj.plugin
        if plugin:
            return obj[plugin]
        else:
            def __call__():
                """No plugin selected"""
                raise NotImplementedError("A plugin must be selected using \'plugin\' field")
            return __call__

class PluginFunctor(object):

    __call__ = PluginFunctorDescriptor()

    def __init__(self, group, brief="", details=""):
        """Create a plugin manager"""
        self._group = group
        self._brief = brief
        self._details = details
        self._cache = dict()

    def __iter__(self):
        def listing():
            for key in self._cache.keys():
                yield key
            for plugin in pkg_resources.iter_entry_points(self._group):
                yield plugin.name
        return sorted(listing()).__iter__()

    def __contains__(self, plugin):
        """
        """
        return plugin in self._cache or len(list(pkg_resources.iter_entry_points(self._group, plugin))) > 0

    def __getitem__(self, plugin):
        """
        """
        while plugin in self._cache:
            plugin = self._cache[plugin]
        if callable(plugin):
            return plugin
        else:
            return pkg_resources.iter_entry_points(self._group, plugin).next().load()

    def __setitem__(self, plugin, implementation):
        if not isinstance(plugin, basestring):
            raise TypeError('\'plugin\' parameter must be a basestring instance')
        if callable(implementation):
            self._cache[plugin] = implementation
        elif isinstance(implementation, basestring):
            if implementation not in self:
                raise ValueError('\'implementation\' parameter must be one of ' + ', '.join('\'' + plugin + '\'' for plugin in self))
            if plugin == implementation:
                raise ValueError('\'plugin\' and \'implementation\' parameters cannot have the same value')
            self._cache[plugin] = implementation
        else:
            raise TypeError('must be callable or a basestring instance')

    @property
    def __doc__(self):
        doc = []
        if self._brief:
            doc.append(self._brief)
            doc.append('')
        if self._details:
            doc.append(self._details)
            doc.append('')
        doc.append(":Available Implementations:")
        doc.extend(" - '" + plugin + "'" for plugin in self)
        return '\n'.join(doc)

    @property
    def plugin(self):
        return getattr(self, '_plugin', None)

    @plugin.setter
    def plugin(self, plugin):
        if plugin not in self:
            raise ValueError('\'plugin\' parameter should be one of ' + ', '.join('\'' + plugin + '\'' for plugin in self))
        else:
            self._plugin = plugin
