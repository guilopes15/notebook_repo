import math
import random

n = float(input('Digite um numero:'))
i = math.trunc(n)
print(f'O numero {n} tem sua parte inteira {i}')
print(f'O arredondamento para cima é {math.ceil(n)}')
print(f'O arredondamento para baixo é {math.floor(n)}')
print(f'Sua raiz quadrada é {math.sqrt(i):.2f}')
print(f'Sua potencia ao quadrado é {math.pow(i,2)}')
print(f'Seu fatorial é {math.factorial(i)}')
print('-' * 20)
an = int(input('Digite um angulo:'))
print(f'Seu seno é {math.sin(math.radians(an)):.2f}')
print(f'Seu cosseno é {math.cos(math.radians(an)):.2f}')
print(f'Sua tangente é {math.tan(math.radians(an)):.2f}')
print('-' * 20)
co = int(input('Digite o cateto oposto:'))
ca = int(input('Digite a cateto adjacente:'))
print(f'Sua hipotenusa é {((co**2+ca**2)**1/2)}')
print('-' * 20)
a1 = str(input('aluno1:'))
a2 = str(input('aluno2:'))
a3 = str(input('aluno3:'))
a4 = str(input(('aluno4:')))
lista = [a1, a2, a3, a4]
random.shuffle(lista)
print(
    f'O aluno escolhido foi {random.choice(lista)}\nA ordem escolhida foi {lista}'
)
