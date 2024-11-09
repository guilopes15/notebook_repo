import sqlite3
from contextlib import ContextDecorator, contextmanager


#manual class context manager
class ContextManager:
    def __init__(self, file_mane, method):
        self.file_obj = open(file_mane, method)

    def __enter__(self):
        return self.file_obj
    
    def __exit__(self, type, value, traceback):
        self.file_obj.close()


class MyContext(ContextDecorator):
    def __enter__(self):
        print('Starting')
        return self

    def __exit__(self, *exc):
        print('Finishing')
        return False
    

@contextmanager
def open_file(name):
    f = open(name, 'w')
    
    try:
        yield f
    
    finally:
        f.close()


#gerador de conexão do DB
@contextmanager
def database(database_url):
    connection = sqlite3.connect(database_url)
    
    try:
        cursor = connection.cursor()
        #delega a conexão para outro recurso
        yield {'connection': connection, 'cursor': cursor}
    
    #exception generica apenas para exemplo. ALTERAR!!
    except Exception as e:
        print(f'an error occurred: {e}') 
    
    finally:
        connection.close()