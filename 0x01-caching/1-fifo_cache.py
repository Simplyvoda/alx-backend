#!/usr/bin/python3
'''
This module contains a function
that inherits from BaseCaching
'''

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    '''
    Implementing First in First Out
    Cache replacement policy
    '''
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        '''
        Assigns to the self.cache_data dict
        the item value for the key
        Dict[Key] = Value
        '''
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                first_key = list(self.cache_data.keys())[0]
                print(f"DISCARD: {first_key}\n")
                del self.cache_data[first_key]

            self.cache_data[key] = item
            return self.cache_data

    def get(self, key):
        '''
        Returns value linked to key in
        self.cache_data
        '''
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
