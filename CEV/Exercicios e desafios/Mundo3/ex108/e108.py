import Modulo
preco = float(input('Digite um preço:'))
print(f'''A metade de {Modulo.moeda(preco)} é {Modulo.moeda(Modulo.metade(preco))}
O dobro de {Modulo.moeda(preco)} é {Modulo.moeda(Modulo.dobro(preco))}
Aumentando 10%, temos {Modulo.moeda(Modulo.porcento(preco,10))}''')
