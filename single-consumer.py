import asyncio

QUEUE_LEN = 10
work_queue = [i for i in range(QUEUE_LEN)]
consumed = 0

async def consumer(name: str):
    global consumed, QUEUE_LEN
    while consumed < QUEUE_LEN:
        item = work_queue[consumed]
        print(f"{name} consumed {item}")
        consumed += 1


async def main():
    await asyncio.gather(
        consumer("A"),
    )

asyncio.run(main())