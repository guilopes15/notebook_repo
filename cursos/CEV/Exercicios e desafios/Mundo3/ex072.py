por_extenso = (
    'zero',
    'um',
    'dois',
    'tres',
    'quatro',
    'cinco',
    'seis',
    'sete',
    'oito',
    'nove',
    'dez',
    'onze',
    'doze',
    'treze',
    'quatrorze',
    'quinze',
    'dezesseis',
    'dezessete',
    'dezoito',
    'dezenove',
    'vinte',
)

while True:
    n = int(input('Digite um numero entre 0 e 20:'))
    if not 0 <= n <= 20:
        n = int(input('Tente novamente. Digite um numero entre 0 e 20:'))
    print(f'Vc digitou o numero {por_extenso[n]}.')
    continuar = str(input('Quer continuar? [S/N]')).upper()
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N]')).upper()
    if continuar == 'N':
        break
