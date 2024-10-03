from dsa.binary_tree.iter import Iter


def height(node):
    height = 0
    for _, info in Iter.pre_order(node):
        height = max(height, info.depth)
    return height


def balance(node):
    if node:
        return height(node.right) - height(node.left)
    else:
        return 0
