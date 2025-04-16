import random

pa = str(input('Primeiro aluno:'))
sa = str(input('Segundo aluno:'))
ta = str(input('Terceiro aluno:'))
qa = str(input(('Quarto aluno:')))
escolha = [pa, sa, ta, qa]
print(f'O aluno escolhido foi {random.choice(escolha)}')

# Pode-se criar uma variavel com a função choice antes do print
