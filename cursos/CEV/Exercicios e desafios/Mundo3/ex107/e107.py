import Modulo
preco = float(input('Digite um preço:'))
print(f'''A metade de {preco} é {Modulo.metade(preco)}
O dobro de {preco} é {Modulo.dobro(preco)}
Aumentando 10%, temos {Modulo.porcento(preco,10)}''')
