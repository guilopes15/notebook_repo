import getpass


try:
    # Solicita uma senha do usuário sem emiti-la.
    senha = getpass.getpass(prompt='senha')

except getpass.GetPassWarning:
    raise UserWarning( 'A senha esta sendo exibida na tela.')

