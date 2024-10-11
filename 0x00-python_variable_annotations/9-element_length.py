#!/usr/bin/env python3
"""Function returns the length of each element in a list."""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Returns a list of tuples containing each element and its length."""
    return [(i, len(i)) for i in lst]
