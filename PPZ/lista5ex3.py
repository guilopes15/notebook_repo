anos = [_ for _ in range(1067, 3628)]
cont = 0

for ano in anos:
    if ano % 2 == 0 and ano % 7 == 0:
        cont += 1
print(cont)