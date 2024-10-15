#!/usr/bin/env python3
"""A Python module collects rand num using an async comprehension."""
import asyncio
from typing import List
from 0_async_generator import async_generator


async def async_comprehension() -> List[float]:
    """
    Collects 10 rand num from async_generator using an async comprehension.
    Returns:
        A list of 10 random float numbers.
    """
    return [number async for number in async_generator()]
