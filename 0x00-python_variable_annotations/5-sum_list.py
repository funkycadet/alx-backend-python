#!/usr/bin/env python3
"""
Complex types - list of floats
"""
from typing import List


def sum_list(input_lists: List[float]) -> float:
    """
    function to return the string representation of a given float argument
    """
    sum_list = 0
    for i in input_lists:
        sum_list += i
    return sum_list
