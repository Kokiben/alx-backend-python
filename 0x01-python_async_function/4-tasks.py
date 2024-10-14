#!/usr/bin/env python3
"""Contains a function that spawns Tasks multiple times with a
specified maximum delay between each call."""
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Creates n tasks using task_wait_random with a specified maximum delay.
    
    Args:
        n: The total number of tasks to create.
        max_delay: The maximum delay for each task.
        
    Returns:
        A list containing the delays in ascending order.
    """
    wait_tasks = [task_wait_random(max_delay) for _ in range(n)]  # Generate the tasks
    return [asyncio.run(wait_task) for wait_task in asyncio.as_completed(wait_tasks)]  # Await and return the completed tasks
