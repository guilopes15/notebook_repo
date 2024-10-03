s = 0
while True:
    n = int(input('Digite um numero:(0 para parar)'))
    if n == 0:
        break
    s += n
print(f'A soma vale {s}')
