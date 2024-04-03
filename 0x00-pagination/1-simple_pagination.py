#!/usr/bin/env python3
"""
Task 1: Simple pagination.
"""
import csv
import math
from typing import Tuple, List


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    returns a tuple of size two containing
    a start index and an end index corresponding
    to the range of indexes to return in a list for
    those particular pagination parameters.
    """
    begin = page_size * (page - 1)
    end = begin + page_size
    return (begin, end)


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
         return the appropriate page of the
         dataset (i.e. the correct list of rows).
        """
        # The assert keyword is used when debugging code.
        # The assert keyword lets you test if a condition
        # in your code returns True, if not, the program will raise
        # an AssertionError.
        self.dataset()
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page_size > 0 and page > 0
        if self.__dataset is None:
            return []
        i, j = index_range(page, page_size)
        return self.__dataset[i:j]
