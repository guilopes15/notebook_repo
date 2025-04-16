peso_maximo = 50
multa = 4
peso_peixe = int(input("Peso do peixe"))
if peso_peixe > peso_maximo:
    excesso = peso_peixe - peso_maximo
    total_multa = excesso * multa
    print(f'A multa foi de {total_multa}.')
else:
    print('Tudo ok')