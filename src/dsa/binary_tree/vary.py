import dsa.binary_tree.find as find


def insert(path, child):
    if path:
        path, found = find.lookup(path, child.value)

        if found:
            return path, False

        parent = path[-1]

        if child.value < parent.value:
            parent.left = child
        else:
            parent.right = child

        path.append(child)

        return path, True

    return [child], True


def delete(path, value):
    if path:
        path, found = find.lookup(path, value)

        if not found:
            return path, None, False

        node = path[-1]

        if node.left and node.right:
            path.append(node.right)
            path = find.min_leaf(path)
            node.value = path[-1].value

        wipe = path.pop()

        desc = wipe.left or wipe.right

        if path:
            parent = path[-1]
            if parent.left is wipe:
                parent.left = desc
            else:
                parent.right = desc

        return path, desc, True

    return [], None, False
