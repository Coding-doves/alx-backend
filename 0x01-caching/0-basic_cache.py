#!/usr/bin/env python3
"""BasicCache module"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    ''' BasicCache '''

    def __init__(self):
        ''' initialiing '''
        super().__init__()

    def put(self, key, item):
        ''' put in cache '''
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        ''' get from cache '''
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data.get(key)
