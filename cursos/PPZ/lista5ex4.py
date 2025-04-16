def sortudo():
    cont = 0
    for num in range(18644, 33088):
        if '2' in str(num) and '7' not in str(num):
             cont += 1
    return cont

print(sortudo())
