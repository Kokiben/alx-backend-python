#!/usr/bin/env python3
"""Contains a function that spawns task_wait_random n times with a
specified delay between each call."""
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random

def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Spawns task_wait_random n times with a specified delay
    between each call.
    
    Args:
        n: The number of times to spawn task_wait_random.
        max_delay: The maximum delay for each random wait.
        
    Returns:
        A list of delays in ascending order.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]  # Create tasks
    return [asyncio.run(task) for task in asyncio.as_completed(tasks)]  # Wait for all tasks to complete
