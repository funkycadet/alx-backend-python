#!/usr/bin/env python3
"""
Complex types - string and int/float to tuple
"""
from typing import List, Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple:
    """
    function tthat takes a string 'k' and an int OR float 'v' as arguments
    and returns a tuple. The first element of the tuple is the string k. The second
    element is the square of the int/float v and would be annotated as a float.
    """
    v = v ** 2
    return (k, v)
