#!/usr/bin/env python3
"""1. FIFO caching"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFOCache that inherits from BaseCaching and is a caching system:
    """

    def __init__(self):
        """initalization"""
        super().__init__()
        self.keys = list()

    def put(self, key, item):
        """
        assign to the dictionary self.cache_data the
        item value for the key key
        """
        if key is not None and item is not None:
            self.cache_data[key] = item
        if key not in self.keys:
            self.keys.append(key)
        if (len(self.keys) > BaseCaching.MAX_ITEMS):
            discard = self.keys.pop(0)
            self.cache_data.pop(discard)
            print(f'DISCARD: {discard}')

    def get(self, key):
        """ return the value in self.cache_data linked to key"""
        if key is None:
            return None
        return self.cache_data.get(key)
