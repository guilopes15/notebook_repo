import secrets
import string


alphabet = string.ascii_letters + string.digits + string.punctuation

password = ''.join(secrets.choice(alphabet) for _ in range(8))

