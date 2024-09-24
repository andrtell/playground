def root(child):
    if child:
        while child.parent:
            child = child.parent
        return child


def lookup(root, data):
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


def succ(root):
    if root:
        if root.right:
            return min_leaf(root.right)
        else:
            while root and root.is_right():
                root = root.parent
            if root and root.parent:
                return root.parent


def pred(root):
    if root:
        if root.left:
            return max_leaf(root.left)
        else:
            while root and root.is_left():
                root = root.parent
            if root and root.parent:
                return root.parent
