#!/usr/bin/env python3
"""
4. MRU Caching
"""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    a class MRUCache that inherits from
    BaseCaching and is a caching system:
    """

    def __init__(self):
        super().__init__()
        self.keys = list()

    def put(self, key, item):
        """
        Must assign to the dictionary self.cache_data
        the item value for the key key
        """
        if key and item:
            self.cache_data[key] = item
            if key not in self.keys:
                self.keys.append(key)
            else:
                self.keys.append(self.keys.pop(self.keys.index(key)))
            if len(self.keys) > BaseCaching.MAX_ITEMS:
                discard = self.keys.pop(-2)
                self.cache_data.pop(discard)
                print(f'DISCARD: {discard}')

    def get(self, key):
        """
        Must return the value in self.cache_data linked to key.
        """
        if key is None or key not in self.cache_data:
            return None
        self.keys.append(self.keys.pop(self.keys.index(key)))
        return self.cache_data.get(key)
