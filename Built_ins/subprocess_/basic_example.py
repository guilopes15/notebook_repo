import subprocess

result = subprocess.run(['git', 'status'])

# Return code 0 -> sucesso
# Return code 1 -> error
print(f'Return code: {result.returncode}')

assert result.returncode == 0


# check=True faz com que lance uma exceção se o comando falhar.
try:
    subprocess.run(["ls", "-l"], check=True)

except subprocess.CalledProcessError:
    print('Error')

