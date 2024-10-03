from .node import Node


class LinkedList:
    def __init__(self):
        self.head = None
        self._size = 0

    def append(self, element):
        # adicionando um novo elemento quando a lista ja tiver elementos
        if self.head:
            ponteiro = self.head
            while ponteiro.next:
                ponteiro = ponteiro.next
            ponteiro.next = Node(element)
        # adicionando um elemento na lista vazia
        else:
            self.head = Node(element)
        self._size += 1

    def __len__(self):
        return self._size

    def _getnode(self, index):
        """Retorna o ponteiro na posição do index passado por parametro."""
        ponteiro = self.head
        for _ in range(index):
            if ponteiro:
                # avançando com o ponteiro se nao tiver vazio
                ponteiro = ponteiro.next
            else:
                raise IndexError('Index out of range')
        return ponteiro

    def __getitem__(self, index):
        ponteiro = self._getnode(index)
        # se o ponteiro nao estiver vazio
        if ponteiro:
            return ponteiro.data
        # o index passado por parametro é maior que o tamanho da lista
        else:
            raise IndexError('Index out of range')

    def __setitem__(self, index, element):
        ponteiro = self._getnode(index)
        # se o ponteiro nao estiver vazio
        if ponteiro:
            # substituindo o elemento
            ponteiro.data = element
        # o index passado por parametro é maior que o tamanho da lista
        else:
            raise IndexError('Index out of range')

    def index(self, elemento):
        ponteiro = self.head
        index = 0
        while ponteiro:
            if ponteiro.data == elemento:
                # retorna o indice do elemento
                return index
            else:
                ponteiro = ponteiro.next
                index += 1
        raise ValueError('element do not exist')

    def insert(self, index, element):
        if index == 0:
            node = Node(element)
            node.next = self.head
            self.head = node
        else:
            # o ponteiro esta apontando para o elemento anterior,
            # para inserir um novo elemento no index passado por parametro
            ponteiro = self._getnode(index - 1)
            node = Node(element)
            node.next = ponteiro.next
            ponteiro.next = node
        self._size += 1

    def remove(self, element):
        if self.head == None:
            raise ValueError('List is empty')
        elif self.head.data == element:
            self.head = self.head.next
            self._size -= 1
            return True

        else:
            ponteiro = self.head.next
            antecessor = self.head
            while ponteiro:
                if ponteiro.data == element:
                    antecessor.next = ponteiro.next
                    ponteiro.next = None
                    return True
                antecessor = ponteiro
                ponteiro = ponteiro.next
            self._size -= 1

        raise ValueError('Element not found')

    def __repr__(self):
        _repr = ''
        ponteirto = self.head
        while ponteirto:
            _repr = _repr + str(ponteirto.data) + ' '
            ponteirto = ponteirto.next
        return _repr

    def __str__(self):
        return self.__repr__()
