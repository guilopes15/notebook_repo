print(
    f"""{'='*20}
Progressão aritimética
{'='*20}"""
)
ptermo = int(input('Primeiro termo:'))
razao = int(input('Razão:'))
for c in range(1, 11):
    pa = ptermo + (c - 1) * razao
    print(f'{pa}', end=' → ')
print('acabou')
