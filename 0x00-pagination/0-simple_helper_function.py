#!/usr/bin/env python3
'''
return a tuple of size two containing a start index/item
and an end index/item
'''
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    '''
    page: to open
    page_size: number of item to display
    
    if page <= 0 or page_size <= 0:
        return None '''

    start_index = (page - 1) * page_size
    end_index = start_index + page_size - 1

    return start_index, end_index
