#!/usr/bin/env python3
"""function safely retrieves a value from a dictionary."""
from typing import Any, Mapping, Optional, TypeVar, Union

T = TypeVar('T')  # Create a TypeVar for the return type


def safely_get_value(dct: Mapping[Any, T], key: Any, default: Optional[T] = None) -> Union[T, None]:
    """Returns the value for the given key if it exists in the dictionary; otherwise, returns the default value."""
    if key in dct:
        return dct[key]
    else:
        return default
