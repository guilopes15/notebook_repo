import Modulo
preco = float(input('Digite um preço:'))
print(f'''A metade de {Modulo.moeda(preco)} é {Modulo.metade(preco,True)}
O dobro de {Modulo.moeda(preco)} é {Modulo.dobro(preco,True)}
Aumentando 10%, temos {Modulo.aumento(preco,10,True)}
Reduzindo 13%, temos {Modulo.desconto(preco,13,True)}''')
