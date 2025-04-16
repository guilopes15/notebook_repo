import datetime

ano = int(input('Ano de nascimento:'))
atual = datetime.date.today().year
idade = atual - ano
calc = idade - 18
sexo = str(input('Qual seu sexo? M/F:')).lower().strip()
if sexo == 'f':
    print('Vc n precisa se alistar')
elif sexo == 'm':
    print(f'Quem naceu em {ano} tem {idade} anos em {atual}.')
    if idade > 18:
        print(
            f"""Voce já de deveria ter se alistado há {idade - 18} anos
Seu alistamento foi em {atual - calc}."""
        )
    elif idade < 18:
        print(
            f"""Ainda faltam {calc} anos para o alistamento
Seu alistamento sera em {calc + atual}."""
        )
    else:
        print('Vc tem q se alistar imediatamente.')
else:
    print('Opção invalida. tente novamente!')
