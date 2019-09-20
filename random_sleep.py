import asyncio
import random

async def random_sleep():
    await asyncio.sleep(random.randint(1,10) / 10.0)

