def find(spine, value):
    if spine:
        while 1:
            last = spine[-1]
            if value < last.value:
                if last.left:
                    spine.append(last.left)
                else:
                    break
            elif value > last.value:
                if last.right:
                    spine.append(last.right)
                else:
                    break
            else:
                return spine, True

    return spine, False


def min_leaf(spine):
    if spine:
        while 1:
            last = spine[-1]
            if last.left:
                spine.append(last.left)
            else:
                break

    return spine


def max_leaf(spine):
    if spine:
        while 1:
            last = spine[-1]
            if last.right:
                spine.append(last.right)
            else:
                break

    return spine


def successor(spine):
    if spine:
        child = spine[-1]
        if child.right:
            spine.append(child.right)
            return min_leaf(spine)
        else:
            spine.pop()
            while spine:
                parent = spine[-1]
                if child is parent.right:
                    child = spine.pop()
                else:
                    break

    return spine


def predecessor(spine):
    if spine:
        child = spine[-1]
        if child.left:
            spine.append(child.left)
            return max_leaf(spine)
        else:
            spine.pop()
            while spine:
                parent = spine[-1]
                if child is parent.left:
                    child = spine.pop()
                else:
                    break

    return spine
