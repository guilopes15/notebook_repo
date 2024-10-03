from binarytree import BinaryTree
from nodebt import NodeTree

ROOT = 'root'


class BinarySeachTree(BinaryTree):
    def insert(self, value):
        parent = None
        aux = self.root
        while aux:
            parent = aux
            if value < aux.data:
                aux = aux.left
            else:
                aux = aux.right
        if parent is None:
            self.root = NodeTree(value)
        elif value < parent.data:
            parent.left = NodeTree(value)
        else:
            parent.right = NodeTree(value)

    def search(self, value):
        return self._search(value, self.root)

    def _search(self, value, node):
        if node is None:
            return node
        if node.data == value:
            return BinarySeachTree(node)
        if value < node.data:
            return self._search(value, node.left)
        else:
            return self._search(value, node.right)

    def minimum(self, node=ROOT):
        if node == ROOT:
            node = self.root
        while node.left:
            if node.left:
                node = node.left
        return node.data

    def maximum(self, node=ROOT):
        if node == ROOT:
            node = self.root
        while node.right:
            if node.right:
                node = node.right
        return node.data

    def remove(self, value, node=ROOT):
        if node == ROOT:
            node = self.root
        if node is None:
            return node
        if value < node.data:
            node.left = self.remove(value, node.left)
        elif value > node.data:
            node.right = self.remove(value, node.right)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                substitute = self.minimum(node.right)
                node.data = substitute
                node.right = self.remove(substitute, node.right)
        return node
