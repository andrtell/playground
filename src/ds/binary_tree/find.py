def lookup(path, value):
    if path:
        while 1:
            root = path[-1]
            if value < root.value:
                if root.left:
                    path.append(root.left)
                else:
                    break
            elif value > root.value:
                if root.right:
                    path.append(root.right)
                else:
                    break
            else:
                return path, True

    return path, False


def min_leaf(path):
    if path:
        while 1:
            root = path[-1]
            if root.left:
                path.append(root.left)
            else:
                break

    return path


def max_leaf(path):
    if path:
        while 1:
            root = path[-1]
            if root.right:
                path.append(root.right)
            else:
                break

    return path


def successor(path):
    if path:
        pred = path[-1]
        if pred.right:
            path.append(pred.right)
            return min_leaf(path)
        else:
            path.pop()
            while path:
                parent = path[-1]
                if pred is parent.right:
                    pred = path.pop()
                else:
                    break

    return path


def predecessor(path):
    if path:
        succ = path[-1]
        if succ.left:
            path.append(succ.left)
            return max_leaf(path)
        else:
            path.pop()
            while path:
                parent = path[-1]
                if succ is parent.left:
                    succ = path.pop()
                else:
                    break

    return path
