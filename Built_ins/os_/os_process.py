import os
import getpass


# Chama comandos do shell diretamente do codigo
os.system('echo Isso é um teste')
os.system('ls') # Insecuro, permite injeção de comandos

# Inicia um novo processo sem esperar ele terminar de forma segura
os.spawnlp(os.P_NOWAIT, "python3", "python3", "--version")  

# Substitui o processo atual e executa outro processo
os.execlp("python3", "python3", "--version")


getpass.getuser() # Retorna o nome do usuario atual
os.getuid()  # Obtem o ID do usuario atual
os.getgid()  # Grupo do usuário atual


# Cria processos filhos sem depender de multiprocessing.
processo_filho = os.fork() 
if processo_filho == 0:
    print("Este é o processo filho")
else:
    print(f"Processo pai, filho tem PID {processo_filho}")


os.nice(10) # Ajusta a prioridade do processo


os.sched_yield() # Cede tempo de CPU para outro processo(Concorrencia).