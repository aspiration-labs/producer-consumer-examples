import asyncio
import datetime
from kombu import Connection

unacked_messages = 0

async def consumer(name: str):
    global unacked_messages
    with Connection('sqs://@') as connection:
        sqs = connection.SimpleQueue('idempotency-demo')
        while unacked_messages > 0:
            message = sqs.get(block=True, timeout=1)
            print(f'{name} received: {message.payload}')
            if name == 'A':
                await asyncio.sleep(1.5)
            message.ack()
            unacked_messages -= 1
        sqs.close()

def publisher(n: int=2):
    global unacked_messages
    with Connection('sqs://@') as connection:
        sqs = connection.SimpleQueue('idempotency-demo')
        for _ in range(n):
            message = f'helloworld, sent at {datetime.datetime.today()}'
            sqs.put(message)
            unacked_messages += 1
            print(f'Sent: {message}')
        sqs.close()

async def main():
    publisher()
    await asyncio.gather(
        consumer("A"),
        consumer("B"),
    )

asyncio.run(main())