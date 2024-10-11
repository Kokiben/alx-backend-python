#!/usr/bin/env python3
"""Function returns a tuple with a string and the square of a number."""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Returns a tuple with the string k and the square of v."""
    return (k, float(v ** 2))
