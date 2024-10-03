num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.sort(reverse=True)
num.insert(2, 2)
if 5 in num:
    num.remove(5)
else:
    print('N achei o numero 5')
print(num)
print(f'Esta lista tem {len(num)} elementos.')
print()

print('-' * 5, 'Criando uma copia entre listas', '-' * 5)
a = [2, 3, 4, 7]
b = a[:]
b[2] = 8
print(
    f"""lista a {a}
lista b {b}"""
)
print()

print('-' * 5, 'Criando uma ligação entre listas', '-' * 5)
a = [2, 3, 4, 7]
b = a
b[2] = 8
print(
    f"""lista a {a}
lista b {b}"""
)
