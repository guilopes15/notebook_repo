import os 
cwd = os.getcwd()


print(os.path.abspath('output.txt'))
print(os.path.exists('output.txt'))
print(os.path.isdir('output.txt'))
print(os.path.isdir(cwd))
print(os.listdir(cwd))


def walk(dirname):
    '''
    Obtem o caminho absoluto de todos os arquivos dentro do diretorio base.
    '''
    for name in os.listdir(dirname):
        path = os.path.join(dirname, name)
        if os.path.isfile(path):
            print(path)
        else:
            walk(path)


walk(cwd)