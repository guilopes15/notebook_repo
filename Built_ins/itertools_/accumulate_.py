from itertools import accumulate

transactions = [200, -100, 300, -200, 100, -50, 300, -150, 200]

extrato = list(accumulate(transactions))

print(extrato)