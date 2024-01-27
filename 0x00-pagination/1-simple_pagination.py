#!/usr/bin/env python3
''' comment '''
import csv
import math
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    '''
    page: to open
    page_size: number of item to display
    '''
    if page <= 0 or page_size <= 0:
        return None

    start_index = (page - 1) * page_size
    end_index = start_index + page_size

    return start_index, end_index
