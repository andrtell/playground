import dsa.binary_tree.iter as iter


def height(node):
    height = 0
    for _, depth in iter.pre_order(node):
        height = max(height, depth)
    return height


def balance(node):
    if node:
        return height(node.right) - height(node.left)
    else:
        return 0
