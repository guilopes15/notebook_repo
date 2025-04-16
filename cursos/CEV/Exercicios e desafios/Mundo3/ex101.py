def voto(ano):
    from datetime import datetime
    idade = datetime.now().year - ano
    if 16 <= idade < 18 or idade > 65:
        condicao = 'Voto Opcional'

    elif idade >= 18:
        condicao = 'Voto Obrigatorio'

    else:
        condicao = 'Não vota'

    return f'Com {idade} anos: {condicao}'


nascimento = int(input('Em que ano vc nasceu?'))
print(voto(nascimento))
