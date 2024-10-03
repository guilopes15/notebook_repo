peso = []
for c in range(1, 6):
    peso.append(float(input(f'Peso da {c}ª pessoa:')))
print(
    f"""O maior peso lido foi de {max(peso)}Kg
O menor peso lido foi de {min(peso)}Kg"""
)

# Resolução do prof
# maior = 0
# menor = 0
# for c in range(1,6)
#   peso = float(input('peso da {c}ª pessoa'))
#   if c == 1 :
#       maior = peso
#       menor = peso
#   else:
#       if peso > maior:
#           maior = peso
#       if peso < menor:
#           menor = peso
# No primeiro if a primeira pessoa recebe tanto o maior quanto o menor peso
# else faz um check nas outras pessoas if peso for maior ou menor
# Entao atribui as variaveis maior e menor nas pessoas subsequentes
