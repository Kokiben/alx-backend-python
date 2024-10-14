#!/usr/bin/env python3
"""Measures the runtime of the wait_n function."""
import asyncio
import time
from typing import List

wait_n = __import__('1-concurrent_coroutines').wait_n

def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the execution time of wait_n(n, max_delay) and returns the average time per call.

    Args:
        n: The number of times to call wait_n.
        max_delay: The maximum delay for each wait_random call.

    Returns:
        The average execution time for each call to wait_n as a float.
    """
    start_time = time.time()  # Start measuring time
    asyncio.run(wait_n(n, max_delay))  # Call the wait_n function
    total_time = time.time() - start_time  # Calculate elapsed time
    return total_time / n  # Return average time per call
