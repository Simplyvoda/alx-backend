#!/usr/bin/python3
'''
This module contains a function
that inherits from BaseCaching
'''

from collections import OrderedDict


BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    '''
    Implementing Last in First Out
    Cache replacement policy
    '''
    def __init__(self):
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        '''
        Assigns to the self.cache_data dict
        the item value for the key
        Dict[Key] = Value
        Checks if dict has exceeded max size
        and deleted using LIFO policy
        '''
        if key is None or item is None:
            return

        if key in self.cache_data:
            del self.cache_data[key]  # Remove the existing key

        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            # accessing key before the item was added
            last_key = list(self.cache_data.keys())[-2]
            print(f"DISCARD: {last_key}\n")
            del self.cache_data[last_key]
            return self.cache_data

    def get(self, key):
        '''
        Returns value linked to key in
        self.cache_data
        '''
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
