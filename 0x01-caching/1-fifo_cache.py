#!/usr/bin/env python3
"""
Task 1: FIFO caching.
"""
from base_caching import BaseCaching
from collections import OrderedDict


class FIFOCache(BaseCaching):
    """
    First In First Out (FIFO) caching.
    Inherits from BaseCaching and is a caching system.
    """
    def __init__(self):
        """
        Init.
        You must use self.cache_data - dictionary
        from the parent class BaseCaching.
        """
        super().__init__()
        # `OrderedDict` maintains the sequence in which keys are added.
        # https://www.geeksforgeeks.org/ordereddict-in-python/
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
        assigns to the cache an item.
        """
        if key is not None and item is not None:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                # for dictionary popitem Pairs are returned
                # in LIFO order if last is true or FIFO order if false.
                first_in, _ = self.cache_data.popitem(False)
                print("DISCARD:", first_in)

    def get(self, key):
        """
        return the value in self.cache_data linked to key.
        """
        return self.cache_data.get(key, None)
