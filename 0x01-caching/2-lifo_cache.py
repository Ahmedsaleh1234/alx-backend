#!/usr/bin/env python3
"""2. LIFO Caching"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """LIFOCache that inherits from
    BaseCaching and is a caching system:"""

    def __init__(self):
        super().__init__()
        self.list_key = ''

    def put(self, key, item):
        """
        assign to the dictionary self.cache_data
        the item value for the key key
        """
        if key is not None and item is not None:
            self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            print(f'DISCARD:{self.list_key}')
            self.cache_data.pop(self.list_key)
        self.list_key = key

    def get(self, key):
        """
        return the value in self.cache_data linked to key.
        """
        if key is None or self.cache_data.get(key) is None:
            return None
        return self.cache_data.get(key)
