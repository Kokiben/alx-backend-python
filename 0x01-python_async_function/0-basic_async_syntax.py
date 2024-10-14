#!/usr/bin/env python3
"""Defines a coroutine that pauses for a random duration and returns that time."""

import asyncio
import random

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
