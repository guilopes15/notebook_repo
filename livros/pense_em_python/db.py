import dbm 

    
def database():
    #dbm é um database de chave e valor
    with dbm.open('legendas', 'c' ) as db:
        db['test'] = 'test123'
        for key in db:
            print(f'{key}: {db[key]}')
