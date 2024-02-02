#!/usr/bin/env python3
"""BasicCache module"""

from base_caching import BaseCaching
from collections import OrderedDict


class LIFOCache(BaseCaching):
    ''' FIFOCache '''

    def __init__(self):
        ''' initialing '''
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        ''' put in cache '''

        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                last_key, _ = self.cache_data.popitem(True)
                print("DISCARD:", last_key)

        if key and item:
            self.cache_data[key] = item
        self.cache_data.move_to_end(key, last=True)

    def get(self, key):
        ''' get from cache '''
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data.get(key)
