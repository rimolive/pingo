import collections
import UserDict


class StrKeyDict(UserDict.UserDict):
    """StrKeyDict always converts non-string keys to `str`

    Tests for item retrieval using `d[key]` notation::

        >>> d = StrKeyDict([('2', 'two'), ('4', 'four')])
        >>> d['2']
        'two'
        >>> d[4]
        'four'
        >>> d[1]
        Traceback (most recent call last):
          ...
        KeyError: '1'

    Tests for the `in` operator::

        >>> 2 in d
        True
        >>> 1 in d
        False

    Test for item assignment using non-string key::

        >>> d[0] = 'zero'
        >>> d['0']
        'zero'

    Tests for update using a `dict` or a sequence of pairs::

        >>> d.update({6:'six', '8':'eight'})
        >>> sorted(d.keys())
        ['0', '2', '4', '6', '8']
        >>> d.update([(10, 'ten'), ('12', 'twelve')])
        >>> sorted(d.keys())
        ['0', '10', '12', '2', '4', '6', '8']
        >>> d.update([1, 3, 5])
        Traceback (most recent call last):
          ...
        TypeError: 'int' object is not iterable

    """

    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]

    def __contains__(self, key):
        return str(key) in self.data

    def __setitem__(self, key, item):
        self.data[str(key)] = item

    def __iter__(self):
        return self.iterkeys()

    def update(self, iterable=None, **kwds):
        if iterable is not None:
            if isinstance(iterable, collections.Mapping):
                pairs = iterable.items()
            else:
                pairs = ((k, v) for k, v in iterable)
            for key, value in pairs:
                self[key] = value
        if kwds:
            self.update(kwds)
