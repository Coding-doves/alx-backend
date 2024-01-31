#!/usr/bin/env python3
"""BasicCache module"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """caching"""

    def __init__(self):
        """Initializes"""
        super().__init__()

    def put(self, key, item):
        """put in cache"""
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """get from cache"""
        return self.cache_data.get(key, None)
