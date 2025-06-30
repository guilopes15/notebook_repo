from asyncio import gather, run
from httpx import AsyncClient

base_url = 'https://pokeapi.co/api/v2/pokemon/{number}'


async def downlaod(number):
    async with AsyncClient() as client:
        response = await client.get(
            base_url.format(number=number),
            timeout=None
        )
        print(number)
        return number, response.json()['name']


# Coloca todas as corrotinas no event loop de uma vez
async def coro(start, stop):
    return await gather(
        *[downlaod(number) for number in range(start, stop)]
    )


result = run(coro(1, 5))
print(result)