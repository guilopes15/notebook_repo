array = [8, 2, 6, 4, 5]
array = sorted(array)
print(array)
words_list = ['expression', 'python', 'Guilherme', 'Spell']
words_list.sort(key=str.upper)
print(words_list)
new_list = sorted(words_list, key=lambda x: x[-1])
print(new_list)
new_list.sort(reverse=True)
print(new_list)


# o metodo .sort() altera a lista original sem criar uma nova e retorna None
# a função sorted() cria e retorna uma nova lista de elementos sem mudar a lista original
# o argumento key define de que maneira a lista vai ser ordenada.
