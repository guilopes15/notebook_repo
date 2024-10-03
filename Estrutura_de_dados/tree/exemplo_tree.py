from binarysearchtree import BinarySeachTree


def exemplo_tree():
    values = [61, 89, 66, 43, 51, 16, 55, 11, 79, 77, 82, 32, 100, 90]
    bst = BinarySeachTree()
    for value in values:
        bst.insert(value)
    return bst


bst = exemplo_tree()
bst.inorder_traversal()
print('\n __________')
bst.level_order_traversal()
print('\n')
print('min:', bst.minimum())
print('max:', bst.maximum())
print('\n')
bst.remove(61)
bst.level_order_traversal()
