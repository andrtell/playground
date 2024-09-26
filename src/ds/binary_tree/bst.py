import ds.binary_tree.find as find

from ds.binary_tree.node import Node

def insert(path, data):
    path, count = find.lookup(path, data)

    if count:
        return path, 0

    child = Node(data)
    
    if path:
        parent = path[-1]

        if data < parent.data:
            parent.left = child
        else:
            parent.right = child

    path.append(child)

    return path, 1


def delete(path, data):
    path, count = find.lookup(path, data)

    if not count:
        return path, 0

    node = path[-1]

    if node.left and node.right:
        path.append(node.right)
        path = find.min_leaf(path)
        node.data = path[-1].data

    wipe = path.pop()

    desc = wipe.left or wipe.right

    if path:
        parent = path[-1]
        if parent.left is wipe:
            parent.left = desc
        else:
            parent.right = desc

    return path, 1
