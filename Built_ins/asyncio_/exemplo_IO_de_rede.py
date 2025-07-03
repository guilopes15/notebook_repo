import asyncio
import itertools
from httpx import AsyncClient
from pathlib import Path
import time


SAVE_DIR = Path('Built_ins/asyncio_/img')


async def spin(msg):  # <1>
    for char in itertools.cycle('|/-\\'):
        status = char + ' ' + msg
        print(status, flush=True, end='\r')
        try:
            await asyncio.sleep(.1)  # <2>
        except asyncio.CancelledError:  # <3>
            break
    print(' ' * len(status), end='\r')


async def fetch(url):
    async with AsyncClient() as client:
        resp = await client.get(url)
        resp.raise_for_status()
        return resp.content
    

async def download(url):
    _bytes = await fetch(url)
    name = Path(url).name
    with open(SAVE_DIR / name, 'wb') as fp:
        fp.write(_bytes)
    return len(_bytes), SAVE_DIR / name


async def supervisor():
    spiner = asyncio.create_task(spin('downloading'))
    url = 'your_url'
    t0 = time.perf_counter()
    size, name = await download(url)
    dt = time.perf_counter() - t0
    spiner.cancel()
    return f'{size:_d} bytes in {dt:0.1f}s\n{name}'


def main():
    msg = asyncio.run(supervisor())
    print(msg)


main()