#!/usr/bin/env python3
"""Contains a function that creates an asyncio.Task from wait_random."""
import asyncio
from typing import Callable

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Creates an asyncio.Task from wait_random.

    Args:
        max_delay: The maximum delay for the random wait.

    Returns:
        An asyncio.Task that wraps the wait_random coroutine.
    """
    return asyncio.create_task(wait_random(max_delay))
