#!/usr/bin/env python3
""" task 0 module """
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """ waits for a random number of seconds """
    i = random.random() * max_delay
    await asyncio.sleep(i)
    return i
