from time import sleep

opcao = 0
while not opcao == 5:
    if opcao != 5:
        pvalor = int(input('Primeiro valor:'))
        svalor = int(input('Segundo valor:'))
        print(
            """    [1] somar
        [2] multiplicar
        [3] maior
        [4] novos numeros
        [5] sair do programa"""
        )
        opcao = int(input('>>>>> Qual é a sua opção?'))
        if opcao == 1 or opcao == 2 or opcao == 3:
            if opcao == 1:
                resultado = pvalor + svalor
                print(f'A soma entre {pvalor} + {svalor} é {resultado}')
            elif opcao == 2:
                resultado = pvalor * svalor
                print(
                    f'A multiplicação entre {pvalor} * {svalor} é {resultado}'
                )
            else:
                if pvalor > svalor:
                    resultado = pvalor
                else:
                    resultado = svalor
                    print(f'O maior entre {pvalor} e {svalor} é {resultado}')
        elif opcao == 4:
            print('Informe os numeros novamente')
        elif opcao != 5:
            print('Opção invalida. tente novamente')
print('Finalizando ....')
sleep(2)
