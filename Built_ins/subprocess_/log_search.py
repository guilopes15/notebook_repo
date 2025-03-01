import subprocess
from pathlib import Path

file_path = Path(__file__).parent / 'my_program.log'

# Lista todas as mensagem que tiverem error
result = subprocess.run(
    f'grep -i error {file_path}'.split(), 
    capture_output=True, 
    text=True,
)

print(f'Achei\n{result.stdout}')

# Executar um comando dentro do shell do sistema
# OBS: Possivel shell injection
result = subprocess.run(f'echo "another log line" >> {file_path}', shell=True)