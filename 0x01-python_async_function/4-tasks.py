#!/usr/bin/env python3
"""Contains a function that spawns multiple Tasks with a
specified maximum delay between each invocation."""
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Creates n tasks using task_wait_random with a specified maximum delay.
    Args:
        n: The number of tasks to create.
        max_delay: The maximum delay for each task.
    Returns:
        A list of delays sorted in ascending order.
    """
    wait_tasks = [task_wait_random(max_delay) for _ in range(n)]
    return [await wait_task for wait_task in asyncio.as_completed(wait_tasks)]
