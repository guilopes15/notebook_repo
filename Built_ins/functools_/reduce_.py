from functools import reduce
from operator import mul


# ((((1 * 2) * 3) * 4) * 5)
reduce(mul, [1, 2, 3, 4, 5]) # Output -> 120

