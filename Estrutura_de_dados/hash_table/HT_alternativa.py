import sys
import os

# Obtém o diretório do arquivo main.py (o diretório atual).
dir_path = os.path.dirname(os.path.realpath(__file__))

# Adiciona o caminho ao diretório do projeto ao sys.path.
sys.path.append(os.path.join(dir_path, '..'))


from linked_list.llist import LinkedList


class HashTable:
    def __init__(self):
        self.MAX = 100
        self.array = self.criar_llist(self.MAX)

    def criar_llist(self, quant):
        ll = LinkedList()
        for _ in range(quant):
            ll.append(None)
        return ll

    def get_hash(self, key):
        hash_ = 0
        for caractere in str(key):
            hash_ += ord(caractere)
        return hash_ % self.MAX

    def __getitem__(self, key):
        index = self.get_hash(key)
        if self.array[index]:
            for item in self.array[index]:
                if key in item:
                    return item
        return None

    def __setitem__(self, key, value):
        index = self.get_hash(key)
        if self.array[index] == None:
            self.array[index] = [key, value]

        elif self.array[index]:
            temp = self.array[index]
            self.array[index] = LinkedList()
            self.array[index].append(temp)
            self.array[index].append([key, value])
        else:
            self.array[index] = [key, value]

    def __delitem__(self, key):
        index = self.get_hash(key)
        if self.array[index]:
            for item in self.array[index]:
                if key in item:
                    try:
                        self.array[index].remove(item)

                    except:
                        self.array[index] = None

                    else:
                        if len(item) == len(key):
                            self.array[index] = None

                    finally:
                        break
        else:
            raise ValueError(f'{key} doesnt not exist')


if __name__ == '__main__':
    t = HashTable()
    t['apple'] = 1
    t['banana'] = 2
    print(t.array)
    del t['apple']
    print(len(t.array))
    print(t.array)
    t['banana'] = 3
    del t['banana']
    del t['banana']
    print(len(t.array))
    print(t.array)
