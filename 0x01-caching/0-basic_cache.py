#!/usr/bin/python3
"""
Task 0: Basic dictionary
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    Basic dictionary.
    Inherits from BaseCaching and is a caching system.
    """

    def put(self, key, item):
        """
        assigns to the cache an item.
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """
        return the value in self.cache_data linked to key.
        """
        return self.cache_data.get(key, None)
