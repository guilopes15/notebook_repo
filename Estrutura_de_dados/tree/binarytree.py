import sys
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(dir_path, '..'))

from nodebt import NodeTree
from my_queue import Queue

ROOT = 'root'


class BinaryTree:
    def __init__(self, data=None, node=None):
        if node:
            self.root = node
        elif data:
            node = NodeTree(data)
            self.root = node
        else:
            self.root = None

    def inorder_traversal(self, node=None):
        if node is None:
            node = self.root
        if node.left:
            self.inorder_traversal(node.left)
        print(node, end=' ')
        if node.right:
            self.inorder_traversal(node.right)

    def postorder_traversal(self, node=None):
        if node is None:
            node = self.root
        if node.left:
            self.postorder_traversal(node.left)
        if node.right:
            self.postorder_traversal(node.right)
        print(node)

    def level_order_traversal(self, node=ROOT):
        if node == ROOT:
            node = self.root
        queue = Queue()
        queue.enqueue(node)
        while len(queue):
            node = queue.dequeue()
            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)
            print(node, end=' ')

    def height(self, node=None):
        if node is None:
            node = self.root

        height_left = 0
        height_right = 0

        if node.left:
            height_left = self.height(node.left)
        if node.right:
            height_right = self.height(node.right)

        if height_left > height_right:
            return height_left + 1
        else:
            return height_right + 1


# tree = BinaryTree()
# node1 = NodeTree('a')
# node2 = NodeTree('+')
# node3 = NodeTree('*')
# node4 = NodeTree('b')
# node5 = NodeTree('-')
# node6 = NodeTree('/')
# node7 = NodeTree('c')
# node8 = NodeTree('d')
# node9 = NodeTree('e')

# node6.left = node7
# node6.right = node8
# node5.left = node6
# node5.right = node9
# node3.left = node4
# node3.right = node5
# node2.left = node1
# node2.right = node3
# tree.root = node2

# tree.simetric_traversal()
def postorder_exemple_tree():
    tree = BinaryTree()
    node1 = NodeTree('i')
    node2 = NodeTree('n')
    node3 = NodeTree('s')
    node4 = NodeTree('c')
    node5 = NodeTree('r')
    node6 = NodeTree('e')
    node7 = NodeTree('v')
    node8 = NodeTree('a')
    node9 = NodeTree('5')
    node0 = NodeTree('3')

    node0.left = node6
    node0.right = node9
    node6.left = node1
    node6.right = node5
    node5.left = node2
    node5.right = node4
    node4.right = node3
    node9.left = node8
    node8.right = node7
    tree.root = node0
    return tree


if __name__ == '__main__':
    tree = postorder_exemple_tree()
    tree.postorder_traversal()
    print(f'Altura: {tree.height()}')
