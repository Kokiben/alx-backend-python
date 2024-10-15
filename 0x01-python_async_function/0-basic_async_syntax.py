#!/usr/bin/env python3
"""Contains a coroutine creates a delay for a random duration and returns."""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Generates a random float value ranging from 0 to max_delay.
    Args:
        max_delay: The maximum possible duration for the random delay.
    Returns:
        float representing actual delay duration within specified range.
    """
    random_delay = random.uniform(0, max_delay)
    await asyncio.sleep(random_delay)
    return random_delay
