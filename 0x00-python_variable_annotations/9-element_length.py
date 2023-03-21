#!/usr/bin/env python3
""" Ducking iterable objects
"""

from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ function to compute the length of a list of sequences.
    """
    return [(i, len(i)) for i in lst]
