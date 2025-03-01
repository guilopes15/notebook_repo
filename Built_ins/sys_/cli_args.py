import sys


print(f"Nome do script: {sys.argv[0]}")
if len(sys.argv) > 1:
    print(f"Argumentos: {sys.argv[1:]}")
else:
    print("Nenhum argumento passado.")

# sys.argv é uma lista onde o primeiro elemento (sys.argv[0]) é o nome do script.

# Nome do script: cli_args.py
# Argumentos: ['argumento1', 'argumento2']


# Se não passarmos argumentos, o programa imprime o erro e encerra.
if len(sys.argv) < 2:
    print("Erro: Argumentos insuficientes.", file=sys.stderr)
    sys.exit(1)  # Código de saída diferente de 0 indica erro.
