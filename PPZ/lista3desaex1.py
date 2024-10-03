triangular = int(input('Digite um numero:'))


def tri(num):
    a = 1
    b = 2
    c = 3
    while True:
        if a * b * c > num:
            condicao = False
            break
        elif a * b * c == num:
            condicao = True
            break
        a += 1
        b += 1
        c += 1
    return condicao


print(tri(triangular))
