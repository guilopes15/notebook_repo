contador = 0
lista = []
soma = 0
for c in range(1, 6):
    n = int(input('Digite um numero:'))
    contador += 1
    soma += n
    lista.append(str(n))
print(
    f"""Os numeros digitados foram {' '.join(lista)}
Ao todo foram {contador} numeros
A soma dos numeros foi {soma}"""
)
