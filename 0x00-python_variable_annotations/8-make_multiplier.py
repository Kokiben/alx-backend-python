#!/usr/bin/env python3
"""Function creates a multiplier function."""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Returns a function multiplies a float by the given multiplier."""
    def multiply(n: float) -> float:
        return n * multiplier
    return multiply
