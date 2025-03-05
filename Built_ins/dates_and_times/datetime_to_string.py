from datetime import date, time, datetime
import locale


hoje = date.today()

# Localiza para o idioma da maquina atual
locale.setlocale(locale.LC_ALL, '')


# O metodo strftime converte e formata datas ou times para strings.
hoje.strftime('%d-%m-%Y')

hoje.strftime('%d de %B de %Y')

hoje.strftime('%A, %d de %B de %Y')


t = time(22,0)
t.strftime('%I:%M:%S %p') # 10:00:00 PM


# Transforma uma string em datetime
str_de_tempo = '3 do 3 de 2025'

datetime.strptime(str_de_tempo, '%d do %m de %Y')


