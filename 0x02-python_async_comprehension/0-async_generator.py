#!/usr/bin/env python3
"""
A coroutine that loops through a certain number and return a random number between 0 - 10
"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:  # Type hint
    """ Async Coroutine """
    for i in range(10):
        await asyncio.sleep(1)  # Pause for 1 second
        yield random.uniform(0, 10)  # yield is how generator produce values,
        # The async doesn't block when yielding a value,
        # the caller of this generator can await each yielding value async..ly
