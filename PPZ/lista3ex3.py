pais1 = 80000
pais2 = 200000
cont = 0

while pais1 < pais2:
    pais1 += pais1 * 0.03
    pais2 += pais2 * 0.015
    cont += 1

print(cont)
