cont = contM = contF = 0
while True:
    print('-' * 20)
    print('Cadastre uma Pessoa')
    print('-' * 20)
    idade = int(input('Idade:'))
    if idade > 18:
        cont += 1
    sexo = ' '
    if sexo not in 'MF':
        sexo = str(input('Sexo: [M/F]')).strip().upper()[0]
        if sexo == 'M':
            contM += 1
        else:
            if idade < 20:
                contF += 1
    continuar = ' '
    if continuar not in 'SN':
        continuar = str(input('Quer continuar?[S/N]')).strip().upper()[0]
    if continuar == 'N':
        break
print(
    f"""Total de pessoas com mais de 18 anos: {cont}
Ao todo temos {contM} homens cadastrados
E temos {contF} mulheres com menos de 20 anos."""
)
