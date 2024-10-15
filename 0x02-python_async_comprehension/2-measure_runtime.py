#!/usr/bin/env python3
"""Python module measures execution time of running async comprehensions."""
import time
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Runs async_comprehension 4 times concurrently and calculates total duration.
    Returns:
        The total time, in seconds, required to complete the four tasks.
    """
    first_time = time.perf_counter()
    a = [async_comprehension() for q in range(4)]
    await asyncio.gather(*a)
    last_time = time.perf_counter()
    return last_time - first_time
