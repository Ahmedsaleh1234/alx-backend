#!/usr/bin/env python3
"""2. LIFO Caching"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """LIFOCache that inherits from
    BaseCaching and is a caching system:"""

    def __init__(self):
        super().__init__()
        self.keys = list()

    def put(self, key, item):
        ''' Add key/value pair to cache data.
            If cache is at max capacity (specified by BaseCaching.MAX_ITEMS),
            discard newest entry in cache to accommodate new entry. '''
        if key is not None and item is not None:
            self.cache_data[key] = item
            if key not in self.keys:
                self.keys.append(key)
            else:
                self.keys.append(self.keys.pop(self.keys.index(key)))
            if len(self.keys) > BaseCaching.MAX_ITEMS:
                discard = self.keys.pop(-2)
                del self.cache_data[discard]
                print('DISCARD: {:s}'.format(discard))

    def get(self, key):
        """ Return value stored in `key` key of cache.
            If key is None or does not exist in cache, return None.
        """
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
