#!/usr/bin/env python3
"""
Complex types - list of floats
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    function to return the sum of a mixed list of floats and integers
    as float
    """
    sum_mixed_list = 0
    for i in mxd_lst:
        sum_mixed_list += i
    return sum_mixed_list
