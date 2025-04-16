# Tipos primitivos (type)
# int - inteiro - Ex:7,-4,0,9875
# float - flutuante(real) - Ex:4.5,0.076,-15.223,7.0
# bool - Ex:True,False (primeira letra sempre maiuscula)
# str - Palavra entre aspas - Ex:'Olá','7.5',''

n = int(input('Digite um valor'))
n2 = float(input('Digite um valor'))
n3 = bool(input('Digite um valor'))
n4 = str(input('Digite um valor'))
print(n, n2, n3, n4)
print(type(n), type(n2), type(n3), type(n4))

# Teste de Tipo
n5 = input('Digite algo')
print(n5.isalnum(), n5.isalpha(), n5.isdecimal(), n5.isnumeric())
