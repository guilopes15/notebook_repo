from itertools import takewhile, dropwhile
from pathlib import Path

# Pegue enquanto verdade
t = takewhile(lambda x: x == 3, [1, 2, 3, 4, 5]) # output -> []
t = takewhile(lambda x: x != 3, [1, 2, 3, 4, 5]) # output -> [1, 2]

t = takewhile(
    lambda x: not x.startswith('#'), 
    open('Built_ins/itertools_/texto.txt')
)

#Nao pega enquanto verdade
d = dropwhile(lambda x: x == 0, [0, 0, 0, 0, 1, 2, 3]) # output -> [1, 2, 3]