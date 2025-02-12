import os
from tempfile import NamedTemporaryFile


with NamedTemporaryFile(delete=False) as temp:
    os.chmod(temp.name, 0o600)  # Apenas o dono pode ler/escrever
