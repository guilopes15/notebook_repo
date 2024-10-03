from linked_list.node import Node


class Stack:
    def __init__(self):
        self.top = None
        self._size = 0

    def push(self, element):
        node = Node(element)
        node.next = self.top
        self.top = node
        self._size += 1

    def pop(self):
        if self._size > 0:
            node = self.top
            self.top = self.top.next
            self._size -= 1
            return node.data
        else:
            raise ValueError('Stack is empty.')

    def peek(self):
        if self._size > 0:
            return self.top.data
        else:
            raise ValueError('Stack is empty.')

    def __len__(self):
        return self._size

    def __repr__(self):
        r = ''
        ponteiro = self.top
        while ponteiro:
            r = r + str(ponteiro.data)
            ponteiro = ponteiro.next
        return r

    def __str__(self):
        return self.__repr__()


pilha = Stack()

pilha.push(1)
pilha.push('Gui')
pilha.push(True)
print(pilha)
print(len(pilha))
print(pilha.peek())
pilha.pop()
print(pilha.peek())
print(pilha)
print(len(pilha))
