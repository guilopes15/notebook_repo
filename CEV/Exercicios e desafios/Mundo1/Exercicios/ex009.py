n = int(input('Digite um numero para ver sua tabuada:'))
print('-' * 12)
print(
    f'{n} x  1 = {n}\n{n} x  2 = {n*2}\n{n} x  3 = {n*3}\n{n} x  4 = {n*4}\n{n} x  5 = {n*5}\n',
    end='',
)
print(
    f'{n} x  6 = {n*6}\n{n} x  7 = {n*7}\n{n} x  8 = {n*8}\n{n} x  9 = {n*9}\n{n} x 10 = {n*10}'
)
print('-' * 12)

# Outra forma de resolver
# n = int(input('Digite um numero para ver sua tabuada'))
# print('{} x {:2} = {}'.format(n,1,n*1)
