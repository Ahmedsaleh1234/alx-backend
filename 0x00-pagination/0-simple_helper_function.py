#!/usr/bin/env python3
"""0. Simple helper function"""

from typing import Tuple


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
