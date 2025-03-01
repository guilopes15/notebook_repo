import subprocess


# subprocess.Popen permiti interação em tempo real com processos
# sem bloquear a execução

# subprocess.PIPE: Permite enviar dados ao processo.
pyenv_process = subprocess.Popen(
    ['pyenv', 'install', '--list'],
      stdout=subprocess.PIPE,
      
)

# O Resultado do pyenv_process é passado como parametro
grep_process = subprocess.Popen(
    ['grep', '3.13'], 
    stdin=pyenv_process.stdout, 
    stdout=subprocess.PIPE,
    text=True
)


# Executa de fato a comunicação entre processos
stdout, stderr = grep_process.communicate()


print(stdout)