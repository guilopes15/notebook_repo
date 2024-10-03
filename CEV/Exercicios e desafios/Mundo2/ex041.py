from datetime import date

ano = int(input('Ano de nascimento:'))
idade = date.today().year - ano
if idade <= 9:
    clas = 'MIRIM'
elif 14 >= idade > 9:
    clas = 'INFANTIL'
elif 19 >= idade > 14:
    clas = 'JÚNIOR'
elif 25 >= idade > 14:
    clas = 'SÊNIOR'
else:
    clas = 'MASTER'
print(
    f"""O atleta tem {idade} anos.
Classificação: {clas}"""
)
