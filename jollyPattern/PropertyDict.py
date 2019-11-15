class PropertyDict(object):
    def __init__(self, *args, **kwargs):
        if len(args) == 1:
            object.__setattr__(self, "_dict", args[0])
        else:
            object.__setattr__(self, "_dict", kwargs)

    def __getattr__(self, name):
        return self._dict[name]

    def __setattr__(self, name, value):
        self._dict[name] = value

    def __str__(self):
        return self._dict.__str__()

    def __repr__(self):
        return self._dict.__repr__()