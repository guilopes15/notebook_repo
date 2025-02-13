import os


'''
 - 0o644:
    Owner: leitura e escrita (6 → 4+2)
    Group: leitura (4)
    Others: leitura (4)
- 0o755:
    Owner: leitura, escrita e execução (7 → 4+2+1)
    Group: leitura e execução (5 → 4+0+1)
    Others: leitura e execução (5)

'''

# Permite alterar as permissões de um arquivo ou diretório.
os.chmod("exemplo.txt", 0o644)