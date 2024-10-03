from linked_list.node import Node


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def enqueue(self, element):
        node = Node(element)
        if self.tail is None:
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        if self.head is None:
            self.head = node
        self._size += 1

    def dequeue(self):
        if self._size > 0:
            element = self.head.data
            self.head = self.head.next
            self._size -= 1
            return element
        else:
            raise ValueError('Queue is empty.')

    def peek(self):
        if self._size > 0:
            return self.head.data
        else:
            raise ValueError('Queue is empty.')

    def __len__(self):
        return self._size

    def __repr__(self):
        r = ''
        ponteiro = self.head
        while ponteiro:
            r = r + str(ponteiro.data) + ' '
            ponteiro = ponteiro.next
        return r

    def __str__(self):
        return self.__repr__()


if __name__ == '__main':
    fila = Queue()

    fila.enqueue(1)
    fila.enqueue('Gui')
    fila.enqueue(True)
    print(fila)
    print(fila.peek())
    fila.dequeue()
    print(fila)
