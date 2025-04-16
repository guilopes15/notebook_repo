n1 = float(input('Digite a primeira nota:'))
n2 = float(input('Digite a segunda nota:'))
m = (n1 + n2) / 2
print(f'Sua media foi {m}')
if m >= 6.0:
    print('Sua media foi boa! Parabéns')
else:
    print('Sua media foi ruim! Estude mais')

# Simplificado
# print('Parabens' if m >= 6.0 else 'Estude mais')
