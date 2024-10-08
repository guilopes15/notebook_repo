import pickle
# o modulo pickle serve para guardar variaveis nao strings em um banco de dados

t1 = [1, 2, 3]

s = pickle.dumps(t1) # transforma qualquer tipo de objeto em uma string 

t2 = pickle.loads(s) # reconstitui o objeto ao tipo original

