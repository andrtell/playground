import ds.binary_tree.find as find


def insert(root, child):
    if not root:
        return child, 1

    parent = root

    while 1:
        if child.data == parent.data:
            return root, 0

        if child.data < parent.data:
            if parent.left:
                parent = parent.left
            else:
                parent.left = child
                break
        else:
            if parent.right:
                parent = parent.right
            else:
                parent.right = child
                break

    return root, 1


def delete(node, path):
    target = node

    if node.left and node.right:
        path.append(node)
        target, path = find.min_leaf(node.right, path)
        node.data = target.data

    child = target.left or target.right

    if path:
        if path[-1].left is target:
            path[-1].left = child
        else:
            path[-1].right = child

        return path[0], 1

    return child, 1
