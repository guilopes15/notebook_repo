cont = 0
s = 0
n = 0
while not n == 999:
    n = int(input('Digite um numero: [999 para parar]'))
    if n != 999:
        cont += 1
        s += n
print(f'Vc digitou {cont} numeros e a soma entre eles foi {s}')
