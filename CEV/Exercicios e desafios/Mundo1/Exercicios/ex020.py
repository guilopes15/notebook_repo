import random

pa = str(input('Primeiro aluno:'))
sa = str(input('Segundo aluno:'))
ta = str(input('Terceiro aluno:'))
qa = str(input('Quarto aluno:'))
ordem = [pa, sa, ta, qa]
random.shuffle(ordem)
print(f'A ordem de apresentação será {ordem}')
