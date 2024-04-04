#!/usr/bin/env python3
"""
Task 3: MRU caching.
"""
from base_caching import BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
    """
    Most Recently Used (MRU) caching.
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
            if key not in self.cache_data:
                if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                    # for dictionary popitem Pairs are returned
                    # in LIFO order if last is true or FIFO order if false.
                    least_used, _ = self.cache_data.popitem(False)
                    print("DISCARD:", least_used)
            self.cache_data[key] = item
            # Move an item to the begining using move_to_end.
            self.cache_data.move_to_end(key, last=False)

    def get(self, key):
        """
        return the value in self.cache_data linked to key.
        """
        # first remove it from least used
        if key is not None and key in self.cache_data:
            self.cache_data.move_to_end(key, last=False)
        return self.cache_data.get(key, None)
