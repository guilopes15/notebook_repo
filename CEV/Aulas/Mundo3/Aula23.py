try:
    a = int(input('Numerador:'))
    b = int(input('Denominador:'))
    r = a / b
except(ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados que vc digitou.')
except ZeroDivisionError:
    print('N é possivel dividir um numero por zero.')
except KeyboardInterrupt:
    print('Informe os dados')
except Exception as erro:
    print(f'O erro encontrado foi {erro.__class__}')
else:
    print(f'O resultado é{r}')
finally:
    print('Obrigado')



#todo linha 11 serve para capturar o erro e instanciar