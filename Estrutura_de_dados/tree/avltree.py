import graphviz
from exemplo_tree import exemplo_tree


def preorder_traversal(tree, dot):
    dot.node(str(tree.data), str(tree.data))
    if tree.left:
        preorder_traversal(tree.left, dot)
        dot.edge(str(tree.data), str(tree.left.data))
    if tree.right:
        preorder_traversal(tree.right, dot)
        dot.edge(str(tree.data), str(tree.right.data))


def to_view(tree, name):
    dot = graphviz.Digraph(comment='Avl_Tree')
    preorder_traversal(tree.root, dot)
    dot.render(f'./tree/{name}.gv', view=True).replace('\\', '/')


tree = exemplo_tree()
to_view(tree, 'viz_avltree')
