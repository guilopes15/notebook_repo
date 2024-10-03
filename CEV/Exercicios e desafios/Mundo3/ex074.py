import random

print('Os valores sorteados foram:', end='')

sorteio = (
    random.randint(0, 10),
    random.randint(0, 10),
    random.randint(0, 10),
    random.randint(0, 10),
    random.randint(0, 10),
)
for n in sorteio:
    print(f' {n} ', end='')
print(f'\nO maior valor sorteado foi {max(sorteio)}')
print(f'O menor valor sorteado foi {min(sorteio)}')

# todo otimizado para lista → sorteio = [randint(0, 10)for c in range(5)]
