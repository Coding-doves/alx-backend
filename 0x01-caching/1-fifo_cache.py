#!/usr/bin/env python3
"""FIFOCache module"""

from base_caching import BaseCaching
from collections import OrderedDict


class FIFOCache(BaseCaching):
    ''' FIFOCache '''

    def __init__(self):
        ''' initialing '''
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        ''' put in cache '''
        if key and item:
            self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_key, _ = self.cache_data.popitem(False)
            print("DISCARD:", first_key)

    def get(self, key):
        ''' get from cache '''
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data.get(key)
