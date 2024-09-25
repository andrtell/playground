def root(child):
    if child:
        while child.parent:
            child = child.parent
    return child


def node(root, data, path=[]):
    while root and root.data != data:
        path.append(root)
        if data < root.data:
            root = root.left
        else:
            root = root.right
    return root, path


def min_leaf(root, path=[]):
    if root:
        while root.left:
            path.append(root)
            root = root.left
    return root, path


def max_leaf(root, path=[]):
    if root:
        while root.right:
            path.append(root)
            root = root.right
    return root, path


def succ(node, path):
    if node:
        if node.right:
            path.append(node)
            return min_leaf(node.right, path)
        else:
            while path:
                parent = path.pop()
                if node is parent.right:
                    node = parent
                else:
                    return parent, path
    return None, []


def pred(node, path):
    if node:
        if node.left:
            path.append(node)
            return max_leaf(node.left, path)
        else:
            while path:
                parent = path.pop()
                if node is parent.left:
                    node = parent
                else:
                    return parent, path
    return None, []
