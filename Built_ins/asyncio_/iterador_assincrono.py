import asyncio


class AsyncIterator:
    def __init__(self):
        self.count = 0

    def __aiter__(self):
        return self

    async def __anext__(self):
        if self.count < 3:
            await asyncio.sleep(1)
            self.count += 1
            return self.count
        else:
            raise StopAsyncIteration


async def exemplo():
    async for i in AsyncIterator():
        print(i)


def is_iterador_assincrono(obj):
    return hasattr(obj, "__aiter__") and hasattr(obj, "__anext__")


asyncio.run(exemplo())
