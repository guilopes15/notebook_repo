import sys
import os

# Obtém o diretório do arquivo (o diretório atual).
dir_path = os.path.dirname(os.path.realpath(__file__))

# Adiciona o caminho ao diretório do projeto ao sys.path.
sys.path.append(os.path.join(dir_path, '..'))


from hash_table.HT_alternativa import HashTable

# from hash_table.my_hashtable import HashTable
from unittest import TestCase


def test_delete_existing_item():
    hash_table = HashTable()
    hash_table['apple'] = 1
    hash_table['banana'] = 2
    h = hash_table.get_hash('banana')
    del hash_table['apple']
    assert 'apple' not in hash_table.array
    assert 'banana' in hash_table.array[h]


def test_delete_non_existing_item():
    hash_table = HashTable()
    hash_table['apple'] = 1
    hash_table['banana'] = 2
    h1 = hash_table.get_hash('apple')
    h2 = hash_table.get_hash('banana')
    with TestCase().assertRaises(ValueError):
        del hash_table['orange']
    assert 'apple' in hash_table.array[h1]
    assert 'banana' in hash_table.array[h2]


def test_delete_item_array_empty():
    hash_table = HashTable()
    hash_table['apple'] = 1
    del hash_table['apple']
    assert 'apple' not in hash_table.array
    assert all(bucket is None for bucket in hash_table.array)


test_delete_existing_item()
test_delete_non_existing_item()
test_delete_item_array_empty()
