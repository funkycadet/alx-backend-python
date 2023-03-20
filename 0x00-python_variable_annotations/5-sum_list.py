#!/usr/bin/env python3
"""
Complex types - list of floats
"""
from typing import List


def sum_list(input_lists: List[float]) -> float:
    """
    function to return the sum of a list of floats as float
    """
    sum_list = 0
    for i in input_lists:
        sum_list += i
    return sum_list
