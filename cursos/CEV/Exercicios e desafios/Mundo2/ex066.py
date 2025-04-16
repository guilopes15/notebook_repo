s = 0
cont = 0
while True:
    v = int(input('Digite um valor (999 para parar):'))
    if v == 999:
        break
    s += v
    cont += 1
print(f'A soma dos {cont} valores foi {s}.')
