cont = 0
continuar = 'S'
n1 = []
if continuar == 'S':
    cont += 1
    while cont > 0:
        n1.append(int(input('Digite um numero:')))
        continuar = str(input('Quer continuar?[S/N]')).strip().upper()[0]
elif continuar == 'N':
    print(
        f"""Vc digitou {cont} numeros e a media foi {sum(n1)/cont}
    O maior valor foi {max(n1)} e o menor {min(n1)}"""
    )
