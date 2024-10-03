import dsa.binary_tree.path as path

def insert(spine, child):
    if spine:
        spine, found = path.find(spine, child.value)

        if found:
            return spine, False

        parent = spine[-1]

        if child.value < parent.value:
            parent.left = child
        else:
            parent.right = child
            
        spine.append(child)

        return spine, True

    return [child], True


def delete(spine, value):
    if spine:
        spine, found = path.find(spine, value)

        if not found:
            return spine, None, False

        node = spine[-1]
        wipe = node

        if node.left and node.right:
            spine.append(node.right)
            spine = path.min_leaf(spine)
            wipe = spine[-1]
            node.value = wipe.value

        spine.pop()

        desc = wipe.left or wipe.right

        if spine:
            parent = spine[-1]
            if parent.left is wipe:
                parent.left = desc
            else:
                parent.right = desc

        return spine, desc, True

    return [], None, False
