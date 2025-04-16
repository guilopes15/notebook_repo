s = 0
maior = 0
homem = ''
cont = 0
for c in range(1, 5):
    print('-' * 5, f'{c}ªPessoa', '-' * 5)
    nome = str(input('Nome:'))
    idade = int(input('Idade:'))
    sexo = str(input('Sexo [M/F]:')).upper()
    s += idade
    if sexo == 'M':
        if c == 1:
            maior = idade
            homem = nome
        else:
            if idade > maior:
                maior = idade
                homem = nome
    else:
        if idade < 20:
            cont += 1
print(
    f"""A media de idade do grupo é de {s/4} anos
O homen mais velho tem {maior} e se chama {homem}
Ao todo são {cont} mulheres com menos de 20 anos"""
)

# todo definindo o maior e o menor sem usar max() e min()
