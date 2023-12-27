#!/usr/bin/env python3
"""
This module contains functions
That handle pagination of a dataset
"""
import csv
import math
from typing import List, Tuple, Dict, Union


def index_range(page: int, page_size: int) -> Tuple[int]:
    """
    This function returns the start and end
    index in a tuple
    """
    start_index = (page * page_size) - page_size
    end_index = (page * page_size)
    return (start_index, end_index)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Handles task 1 requirement
        """
        assert isinstance(page, int) and page > 0, \
            "Page number should be a positive integer"
        assert isinstance(page_size, int) and page_size > 0, \
            "Page size should be a positive integer"

        self.__page = page
        self.__page_size = page_size

        start_index, end_index = index_range(page, page_size)
        dataset = self.dataset()

        if start_index >= len(dataset):
            return []

        return dataset[start_index:end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> \
            Dict[str, Union[int, List[Union[str, int]], int]]:
        """
        Handle task 2 requirement
        """
        assert isinstance(page, int) and page > 0, \
            "Page number should be a positive integer"
        assert isinstance(page_size, int) and page_size > 0, \
            "Page size should be a positive integer"

        self.__page = page
        self.__page_size = page_size

        data = self.get_page(page, page_size)
        complete_data = self.dataset()

        if len(data) == 0:
            dict_page_size = 0
            dict_next_page = None
        else:
            dict_page_size = self.__page_size
            dict_next_page = self.__page + 1

        dict_total_pages = round(len(complete_data)/self.__page_size)

        if self.__page == 1:
            dict_prev_page = None
        else:
            dict_prev_page = self.__page - 1

        new_dict = {'page_size': dict_page_size, 'page': self.__page,
                    'data': data, 'next_page': dict_next_page,
                    'prev_page': dict_prev_page,
                    'total_pages': dict_total_pages}

        return new_dict
