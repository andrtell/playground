import ds.binary_tree.find as find


def insert(path, child):
    if path:
        parent = path[-1]

        if child.data < parent.data:
            parent.left = child
        else:
            parent.right = child

        for node in reversed(path):
            node.update()

        path.append(child)

        return path, 1

    return [child], 1


def delete(path):
    if path:
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

        for node in reversed(path):
            node.update()

        if desc:
            path.append(desc)

        return path, 1

    return [], 0
