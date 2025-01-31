from itertools import islice


generator = (x for x in range(10))

# Slice de generator
g_slice = islice(generator, 0, 5) # Use None para ir ate o fim da sequencia.

print(next(g_slice))
