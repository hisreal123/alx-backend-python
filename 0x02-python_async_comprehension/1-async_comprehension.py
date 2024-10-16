#!/usr/bin/env python3
"""
A coroutine that loops through a certain number and return a random number between 0 - 10
"""
async_generator = __import__('0-async_generator').async_generator
from typing import List


async def async_comprehension() -> List[float]:
    randon_number = [i async for i in async_generator()]
    return randon_number
