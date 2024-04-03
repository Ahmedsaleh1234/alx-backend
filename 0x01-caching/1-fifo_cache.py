#!/usr/bin/env python3
"""1. FIFO caching"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFOCache that inherits from BaseCaching and is a caching system:
    """

    def put(self, key, item):
        """
        assign to the dictionary self.cache_data the
        item value for the key key
        """
        if key is None and item is None:
            return
        if (len(self.cache_data) > BaseCaching.MAX_ITEMS):
            frist_item = next(iter(self.cache_data))
            self.cache_data.pop(frist_item)
        self.cache_data[key] = item

    def get(self, key):
        """ return the value in self.cache_data linked to key"""
        if key is None:
            return None
        return self.cache_data.get(key)
