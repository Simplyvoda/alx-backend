#!/usr/bin/python3
'''
This module contains a function
that inherits from BaseCaching
'''

import time


BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    '''
    Implementing Least Recently Used
    Cache replacement policy
    '''
    def __init__(self):
        super().__init__()
        self._temp_dict = {}

    def put(self, key, item):
        '''
        Assigns to the self.cache_data dict
        the item value for the key
        Dict[Key] = Value
        Checks if dict has exceeded max size
        and deleted using LRU policy
        '''
        if key is None or item is None:
            return

        if key in self.cache_data:
            del self.cache_data[key]  # Remove the existing key

        self.cache_data[key] = item
        # setting dictionary to hold time
        self._temp_dict[key] = time.time()

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            # getting current time
            current_time = time.time()
            max_diff_key = None
            max_time_difference = float('-inf')
            # looping through values to find the oldest time
            for cache_key, cache_time in self._temp_dict.items():
                time_difference = current_time - cache_time
                if time_difference > max_time_difference:
                    max_time_difference = time_difference
                    max_diff_key = cache_key
            print(f"DISCARD: {max_diff_key}\n")
            # delete key from 2 dictionaries
            del self.cache_data[max_diff_key]
            del self._temp_dict[max_diff_key]
            return self.cache_data

    def get(self, key):
        '''
        Returns value linked to key in
        self.cache_data
        '''
        if key is not None and key in self.cache_data:
            self._temp_dict[key] = time.time()
            return self.cache_data[key]
        return None
