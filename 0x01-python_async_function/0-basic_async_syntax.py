#!/usr/bin/env python3
import random

async def wait_random(max_delay: int = 10):
    i = random.randint(0, max_delay)
    return i
