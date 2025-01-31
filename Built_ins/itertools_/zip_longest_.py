from math import nan
from itertools import zip_longest

ES = (22, 26, 18)
MG = (16, 20, 29, 18, 14)
RJ = (22, 17, 26, 19, 24)
SP = (31, 27, 29, 17, 19)

# Zipa os valores e adiciona nan nos espaços vazios
print(tuple(zip_longest(ES, MG, RJ, SP, fillvalue=nan))) 
