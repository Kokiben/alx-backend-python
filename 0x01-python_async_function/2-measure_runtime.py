#!/usr/bin/env python3
"""Contains a method that measures the total execution time of
a function."""
from time import perf_counter
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Measure the total execution time of a function.
    Args:
        n: The number of coroutines to launch.
        max_delay: The maximum amount of time to wait for each coroutine.
    Returns:
        Elapsed time in seconds.
    """
    start_time = perf_counter()  # Start time measurement
    asyncio.run(wait_n(n, max_delay))  # Run the wait_n function
    ep_time = perf_counter() - start_time  # Calculate elapsed time
    return ep_time / n  # Return average time per coroutine
