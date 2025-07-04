import asyncio
from functools import wraps


def tornar_assincrona(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        loop = asyncio.get_running_loop()
        return await loop.run_in_executor(None, func, *args, **kwargs)
    return wrapper


@tornar_assincrona
def func_sincrona(x, y):
    import time
    time.sleep(1)
    return x + y


async def main():
    resultado = await func_sincrona(10, 20)
    print(resultado)


def is_func_assincrona(obj):
    return hasattr(obj, "__await__")


asyncio.run(main())