from functools import lru_cache
from time import sleep
from functools import cache


@lru_cache(maxsize=2)
def id_delay(x):
    sleep(3)
    return x


id_delay(1) # Demora 3 sec
id_delay(3) # Demora 3 sec
id_delay(1) # Usa o cache
id_delay(3) # Usa o cache


@cache
def factorial(n):
    return n * factorial(n-1) if n else 1