import os
# Pipes


cmd = 'ls'
fp = os.popen(cmd)

# Com o os.popen é possivel executar comando do shell atraves de codigo.
# O objeto de retorno se comporta como um arquivo aberto, 
# podendo entao utilizar o metodo read() ou readlines() por exemplo. 