#!/usr/bin/env python3
"""Contains a coroutine that creates a delay for a random duration and returns that duration."""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Generates a random float value ranging from 0 to max_delay.
    
    Args:
        max_delay: The maximum possible duration for the random delay.
        
    Returns:
        A float representing the actual delay duration within the specified range.
    """
    random_delay = random.uniform(0, max_delay)  # Generate a random float within the specified range
    await asyncio.sleep(random_delay)  # Pause execution for the random duration
    return random_delay  # Return the generated delay duration
