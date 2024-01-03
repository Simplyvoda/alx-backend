#!/usr/bin/python3
'''
This module contains a function
that inherits from BaseCaching
'''

from collections import OrderedDict

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
  '''
    Implementing First in First Out
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
        Checks if the dict has exceeded max size
        and deletes using FIFO policy
        '''
    if key is None or item is None:
      return

    self.cache_data[key] = item

    if len(self.cache_data) > BaseCaching.MAX_ITEMS:
      first_key = list(self.cache_data.keys())[0]
      print(f"DISCARD: {first_key}\n")
      del self.cache_data[first_key]
      return self.cache_data
    return self.cache_data

  def get(self, key):
    '''
        Returns value linked to key in
        self.cache_data
        '''
    if key is not None and key in self.cache_data:
      return self.cache_data[key]
    return None
