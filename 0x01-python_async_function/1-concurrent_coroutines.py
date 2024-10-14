#!/usr/bin/env python3
"""Defines a method that initiates wait_random n times with a
specified delay between each invocation."""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Initiates wait_random n times with a given maximum delay
    for each call.

    Args:
        n: The number of times to invoke wait_random.
        max_delay: The upper limit for the delay for each call.

    Returns:
        A list of delay durations in ascending order.
    """
    delay_tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    delay_times = [await delay_task for delay_task in asyncio.as_completed(delay_tasks)]
    return delay_times
