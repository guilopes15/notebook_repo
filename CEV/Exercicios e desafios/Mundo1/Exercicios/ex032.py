import datetime

y = int(input('Que ano quer analisa? Coloque 0 para analisar o ano atual:'))
if y == 0:
    y = datetime.date.today().year
if y % 4 == 0 and y % 100 != 0 or y % 400 == 0:
    print(f'O ano {y} é Bissexto')
else:
    print(f'O ano {y} nao é Bissexto')
