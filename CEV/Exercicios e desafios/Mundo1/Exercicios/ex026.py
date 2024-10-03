frase = str(input('Digite uma frase:')).strip().upper()
print(f"A letra A aparece {frase.count('A')}")
print(f"A primeira letra A apareceu na posição {frase.find('A')+1}")
print(f"A ultima letra A apareceu na posição {frase.rfind('A')+1}")
