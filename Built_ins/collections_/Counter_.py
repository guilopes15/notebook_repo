from collections import Counter


texto = "banana"

# Usado para contar ocorrências de elementos em uma sequência.
contagem = Counter(texto)

print(contagem)  # output -> {'b': 1, 'a': 3, 'n': 2}


Counter('abc') & Counter('bdc') # Intersecção

# Retorna uma lista dos 3 elementos mais comuns e suas contagens, 
# do mais comum para o menos comum.
Counter('abracadabra').most_common(3)


c = Counter(a=4, b=2, c=0, d=-2)
d = Counter(a=1, b=2, c=3, d=4)

# Subtrai os elementos de acordo com sua key.
c.subtract(d) # output -> {'a': 3, 'b': 0, 'c': -3, 'd': -6}

# Soma todos os elementos
c.total() 