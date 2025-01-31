from itertools import repeat


for x in repeat('python', 5): #Tbm um jeito de fazer while True.
    print(x)


p = list(map(pow, repeat(2), range(12)))

print(p)