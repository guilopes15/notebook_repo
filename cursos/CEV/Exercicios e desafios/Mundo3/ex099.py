from time import sleep


def maior(*n):
    print('Analisando os valores passados ...')
    for v in n:
        print(f'{v} ', end='')
        sleep(0.3)
    if n:
        cont = len(n)
        maior = max(n)
    else:
        cont = 0
        maior = 0
    print(
        f"""Foram informados {cont} valores ao todo.
O maior valor informado foi {maior}"""
    )
    print('-' * 30)


print('-' * 30)
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
