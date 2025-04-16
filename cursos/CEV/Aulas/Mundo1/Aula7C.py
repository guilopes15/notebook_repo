n1 = int(input('Digite um numero:'))
n2 = int(input('Digite outro numero:'))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
p = n1**n2
print(
    f'A soma é {s}, a multiplicação é {m} \nA divisão é {d:.3f}', end=' >>> '
)
print('a divisão inteira é {} e a potência é {}'.format(di, p))
