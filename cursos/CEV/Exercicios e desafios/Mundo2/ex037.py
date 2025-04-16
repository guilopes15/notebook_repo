n = int(input('Digite um numero inteiro:'))
b = 'Binario'
o = 'Octal'
h = 'Hexadecimal'
print(
    f"""[1] converter para {b}
[2] converter para {o}
[3] converter para {h}"""
)
op = int(input('Sua opção:'))
if op == 1:
    print(f'{n} convertido para {b} é igual a {bin(n)[2:]}')
elif op == 2:
    print(f'{n} convertido para {o} é igual a {oct(n)[2:]}')
elif op == 3:
    print(f'{n} convertido para {h} é igual a {hex(n)[2:]}')
else:
    print('Opção invalida. Tente novamente.')
