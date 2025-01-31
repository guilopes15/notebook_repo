from itertools import starmap
from operator import mul


pairs = [(2,5),(3,4),(8,6),(7,3)]

products = map(mul, pairs) # Error

products = starmap(mul, pairs)
