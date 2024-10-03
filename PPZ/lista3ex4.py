fibonacci = int(input("Quantos numeros na sequenci de fibinacci?"))
a, b = 1, 1
print(a, b, end=' ')
while fibonacci - 2 > 0:
    a, b = b, a + b
    fibonacci -= 1
    print(b, end=' ')
