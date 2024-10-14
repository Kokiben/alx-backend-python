#!/usr/bin/env python3
"""Defines a coroutine that waits for a random delay and returns it."""

import asyncio
import random

async def wait_random(max_delay: int = 10) -> float:
    """Pauses execution for a random duration between 0 and max_delay seconds, then returns the duration."""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
