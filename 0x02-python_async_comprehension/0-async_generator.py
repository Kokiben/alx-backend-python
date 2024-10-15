#!/usr/bin/env python3
"""A Python module that yields random numbers asynchronously."""
import random
import asyncio
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Asynchronously generates 10 random numbers.
    Yields a random float between 0 and 10 after waiting for 1 second,
    repeated 10 times.
    """
    for a in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
