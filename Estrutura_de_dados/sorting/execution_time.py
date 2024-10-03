from typing import Callable
from random import randint
from timeit import repeat


def sorting_algorithm_time(
    algorithm: Callable[[], list] | str, array: list
) -> None:
    """Mede o tempo minimo de execução de uma função de ordenação.

    Args:
        algorithm (callable): Função de ordenação
        array (list): Lista de numeros para serem ordenados
    Vars:
        setup: importa a função que vai ser executada,
        só é necessario de for um algoritmo de ordenação personalizado,
        se for built-in por defaut é pass.
        stmt: é a funçao e os argumentos que o repeat vai executar.
        times: arnazena o retorno do repeat, que é uma list.
    """
    setup = (
        f'from __main__ import {algorithm}' if algorithm != 'sorted' else ''
    )

    stmt = f'{algorithm}({array})'
    times = repeat(setup=setup, stmt=stmt, repeat=3, number=10)

    print(f'Algotithm:{algorithm}. Minimum execution time:{min(times)}')


if __name__ == '__main__':
    lista = [randint(0, 100) for _ in range(42)]
    sorting_algorithm_time('sorted', lista)
