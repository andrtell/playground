def root(child):
    if child:
        while child.parent:
            child = child.parent
    return child


def node(root, data):
    while root and root.data != data:
        if data < root.data:
            root = root.left
        else:
            root = root.right

    return root


def min_leaf(root):
    if root:
        while root.left:
            root = root.left
    return root


def max_leaf(root):
    if root:
        while root.right:
            root = root.right
    return root


def succ(node):
    if node:
        if node.right:
            return min_leaf(node.right)
        else:
            while node and node.is_right():
                node = node.parent

            return node and node.parent


def pred(node):
    if node:
        if node.left:
            return max_leaf(node.left)
        else:
            while node and node.is_left():
                node = node.parent

            return node and node.parent
