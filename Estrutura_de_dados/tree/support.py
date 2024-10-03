from binarytree import BinaryTree
from nodebt import NodeTree


#       '+'
#     /     \
#   'a'     '*'
#          /   \
#        'b'   '-'
#             /   \
#           '/'   'e'
#          /   \
#        'c'   'd'
#
# (a + (b * ((c / d) - e)))

tree = BinaryTree()
node1 = NodeTree('a')
node2 = NodeTree('+')
node3 = NodeTree('*')
node4 = NodeTree('b')
node5 = NodeTree('-')
node6 = NodeTree('/')
node7 = NodeTree('c')
node8 = NodeTree('d')
node9 = NodeTree('e')

node6.left = node7
node6.right = node8
node5.left = node6
node5.right = node9
node3.left = node4
node3.right = node5
node2.left = node1
node2.right = node3
tree.root = node2
