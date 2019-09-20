import asyncio
from random_sleep import random_sleep

QUEUE_LEN = 10
work_queue = [i for i in range(QUEUE_LEN)]
consumed = 0

async def consumer(name: str):
    global consumed, QUEUE_LEN
    while consumed < QUEUE_LEN:
        await random_sleep()
        # Think: Message Received
        item = work_queue[consumed]
        print(f"{name} consumed {item}")
        await random_sleep()
        # Think: Message Acknowledged
        consumed += 1


async def main():
    await asyncio.gather(
        consumer("A"),
        consumer("B"),
    )

asyncio.run(main())