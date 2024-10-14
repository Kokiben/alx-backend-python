#!/usr/bin/env python3
"""Defines a coroutine that waits for a random duration and returns that time."""

import asyncio
import random
from typing import List

async def wait_random(max_delay: int = 10) -> float:
    """
    Generates a random wait time between 0 and max_delay seconds and pauses for that duration.
    
    Args:
        max_delay: The maximum number of seconds to wait.
        
    Returns:
        The generated random float representing the wait time.
    """
    wait_time = random.uniform(0, max_delay)
    await asyncio.sleep(wait_time)
    return wait_time

async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns wait_random n times with the specified max_delay and returns a list of delays in ascending order.
    
    Args:
        n: The number of times to call wait_random.
        max_delay: The maximum delay to be used for wait_random.
        
    Returns:
        A list of all the delays in ascending order.
    """
    delays = []
    for _ in range(n):
        delays.append(asyncio.create_task(wait_random(max_delay)))
    
    # Gather all results as they complete
    completed_delays = []
    for task in asyncio.as_completed(delays):
        completed_delay = await task
        completed_delays.append(completed_delay)
    
    return completed_delays
