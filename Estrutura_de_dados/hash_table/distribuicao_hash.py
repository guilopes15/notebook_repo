from collections import Counter
from string import printable


def distruibuicao(items, num_conteiners, hast_funcition=hash):
    return Counter([hast_funcition(item) % num_conteiners for item in items])


def plot(histograma):
    for key in sorted(histograma):
        count = histograma[key]
        padding = (max(histograma.values()) - count) * ' '
        print(f'{key:3} {"■" * count} {padding} ({count})')


plot(distruibuicao(printable, num_conteiners=2))

plot(distruibuicao(printable, num_conteiners=5))
