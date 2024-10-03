n = input('Digite algo:')
print(type(n))
print(
    'É numerico? {}\nÉ alpha? {}\nSó tem espaços? {}\n'.format(
        n.isnumeric(), n.isalpha(), n.isspace()
    )
)
print(
    f'É numerico? {n.isnumeric()}\nÉ alpha? {n.isalpha()}\nSó tem espaços? {n.isspace()}'
)

m = int(input('Digite um numero:'))
a = int(-1)
b = int(+1)
print(f'Analisando o valor {m}, seu antecessor é {m-1} e o sucessor é {m+1}')
