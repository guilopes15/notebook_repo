lista = []
lista_par = []
lista_impar = []
while True:
    n = int(input('Digite um numero:'))
    lista.append(n)
    continuar = str(input('Quer continuar?[S/N]')).upper().strip()[0]
    while continuar not in 'SN':
        print('Resposta invalida')
        continuar = str(input('Quer continuar?[S/N]')).upper().strip()[0]
    if n % 2 == 0:
        lista_par.append(n)
    else:
        lista_impar.append(n)
    if continuar == 'N':
        break
print('-=' * 30)
print(
    f"""A lista completa é {lista}
A lista de pares é {lista_par}
A lista de impares é {lista_impar}"""
)

# todo para verificar se a resposta é S ou N, a variavel continuar tem q estar
# declarada dentro do input no while True, antes do segundo while da verificação.
