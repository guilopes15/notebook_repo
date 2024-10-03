p = str(input('Digite algo:')).lower()
vogais = 'aeiou'
if p.count(' ') > 0:
    status = 'É uma frase!'
else:
    status = 'É uma palavra'
print(f'{status}')
if 'a' or 'e' or 'i' or 'o' or 'u' in p:
    print('E as vogais sao: ', end='')
    for vogal in vogais:
        if p.find(f'{vogal}') != -1:
            print(f'{vogal} → ', end='')
else:
    print('N tem vogal')
