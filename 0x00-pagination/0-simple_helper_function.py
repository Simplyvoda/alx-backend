#!/usr/bin/env python3
"""
This module contains a function
that returns the start and end index
to return in a list
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int]:
    """
    This function returns the start and end
    index in a tuple
    """
    start_index = (page * page_size) - page_size
    end_index = (page * page_size)
    return (start_index, end_index)
