#!/usr/bin/env python3
"""Let's execute multiple coroutines at the same time with
async."""
from time import perf_counter
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """spawn wait_random n times with the specified max_delay.
    Args:
        n: num of coroutines.
        max_delay: maximum amount of time for each coroutine.
    Returns:
        Elapsed time in sec.
    """
    start_time = perf_counter()  # Start time measurement
    asyncio.run(wait_n(n, max_delay))  # Run the wait_n function
    ep_time = perf_counter() - start_time  # Calculate elapsed time
    return ep_time / n  # Return average time per coroutine
