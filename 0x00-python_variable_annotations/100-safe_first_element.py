#!/usr/bin/env python3
""" Duck typing - first elements of a sequence
"""

from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """ function to retrieve the first element of an existing sequence
    """
    if lst:
        return lst[0]
    else:
        return None
