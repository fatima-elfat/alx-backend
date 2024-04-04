#!/usr/bin/env python3
"""
Task 3: LFU caching.
"""
from base_caching import BaseCaching
from collections import OrderedDict


class LFUCache(BaseCaching):
    """
    Least Frequently Used (LFU) caching.
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
        self.frequently = dict()
        for k in self.cache_data:
            self.frequently[k] = 0

    def put(self, key, item):
        """
        assigns to the cache an item.
        """
        if key is not None and item is not None:
            if key not in self.cache_data:
                if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                    # for dictionary popitem Pairs are returned
                    # in LIFO order if last is true or FIFO order if false.
                    ordered_l = sorted(
                        self.frequently.items(),
                        key=lambda x: x[1])
                    key_, _ = list(ordered_l)[0]
                    self.cache_data.pop(key_)
                    self.frequently.pop(key_)
                    print("DISCARD:", key_)
                self.frequently[key] = 0
            self.cache_data[key] = item
            self.frequently[key] += 1

    def get(self, key):
        """
        return the value in self.cache_data linked to key.
        """
        # first remove it from least used
        if key is not None and key in self.cache_data:
            self.frequently[key] += 1
        return self.cache_data.get(key, None)
