#!/usr/bin/env python3
"""1-simple_pagination.py"""

import csv
import math
from typing import List, Tuple, Dict
import math


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Function: Caluclate the frist and index to specific page
    page: the last page
    page_size: the item that found in page
    Return: A tuple of frist and last index
    """
    frist_index = (page - 1) * page_size
    end_index = frist_index + page_size
    return (frist_index, end_index)


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
        Function: find the correct indexes to paginate the dataset
        """
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0
        start, end = index_range(page, page_size)
        data = self.dataset()
        if start > len(data):
            return []
        return data[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """
        returns a dictionary containing the following key-value pairs:
        """
        data = self.get_page(page, page_size)
        data_len = self.dataset()
        start, end = index_range(page, page_size)
        next_page = page + 1
        if end >= len(data_len):
            next_page = None
        prev_page = page - 1
        if start <= 0:
            prev_page = None
        total_pages = math.ceil((len(data_len)) / page_size)

        return {
            'page_size': len(data),
            'page': page,
            'data': data,
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': total_pages
        }
