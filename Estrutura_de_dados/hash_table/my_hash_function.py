def hash_function(text):
    return sum(
        index * ord(character)
        for index, character in enumerate(repr(text).lstrip("'"), start=1)
    )


t1 = hash_function('teste')
t2 = hash_function('Tiny') % 100
t3 = hash_function('This has a somewhat medium length.') % 100
t4 = hash_function('This is very long and slow!' * 1_000_000) % 100

print(f'{t1}\n {t2}\n {t2}\n {t3}\n {t4}\n')
