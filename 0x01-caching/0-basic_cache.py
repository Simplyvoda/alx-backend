#!/usr/bin/python3
'''
This module contains a function
that inherits from BaseCaching
'''

BaseCaching = __import__('base_caching').BaseCaching

class BasicCache(BaseCaching):
  '''
  This class contains 2 methods
  put - acts as a setter method
  get - acts as a getter method
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
      self.cache_data[key] = item
      return self.cache_data

  def get(self,key):
    '''
    Returns value linked to key in
    self.cache_data
    '''
    if key is not None and key in self.cache_data:
      return self.cache_data[key]
    return None