continuar = ''
lista = []
while True:
    n = int(input('Digite um valor:'))
    if n not in lista:
        lista.append(n)
        print('Valor adicionado com sucesso')
    else:
        print('Valor duplicado')

    continuar = str(input('Quer continuar?[S/N]')).strip().upper()
    if continuar == 'N':
        break
lista.sort()
print(lista)
