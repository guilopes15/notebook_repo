#lista/fila/pilha
from collections import deque


container = deque(maxlen=3)

container.append(1) # Adiciona na direita

container.appendleft(2) # Adiciona na esquerda

container.popleft() # Remove da esquerda(Fila)

container.pop()# Remove da direita(Pilha)

container.reverse() # Inverte o container


# Gira o container n passos para a direita. 
# Se n for negativo, gire para a esquerda.
container.rotate(n=1) 

