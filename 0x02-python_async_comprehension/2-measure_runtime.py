#!/usr/bin/env python3
"""A Python module measures runtime of running async comprehensions."""
import asyncio
import time
from typing import List
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measures the total runtime of executing four times in parallel.
    Uses asyncio.gather to run four instances of concurrently.
    Returns:
        The total runtime in seconds as a float.
    """
    start_time = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for q in range(4)))
    end_time = time.perf_counter()
    return end_time - start_tiqe
