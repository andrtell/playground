import ds.binary_tree.bst as bst


def insert(path, child):
    path, count = bst.insert(path, child)

    if not count or abs(path[0].balance) < 2:
        return path, count

    new_path = [path.pop(), path.pop(), path.pop()]

    j = len(path)

    while j >= 0:
        p = new_path[-1]
        c = new_path[-2]

        if p.right is c:
            if p.balance < -1:
                if c.balance > 0:
                    new_path = rotate_right_left(new_path)
                else:
                    new_path = rotate_left(new_path)
            elif p.balance == 0:
                break
        else:
            if p.balance > 1:
                if c.balance < 0:
                    new_path = rotate_left_right(new_path)
                else:
                    new_path = rotate_right(new_path)
            elif p.balance == 0:
                break

        if path:
            r = path.pop()
            if r.left is p:
                r.left = new_path[-1]
            else:
                r.right = new_path[-1]
            r.update()
            new_path.append(r)

        j -= 1

    new_path.reverse()

    path.extend(new_path)

    return path, 1


def delete(path):
    path, count = bst.delete(path)

    if not count or abs(path[0].balance) < 2:
        return path, count

    new_path = [path.pop(), path.pop(), path.pop()]

    j = len(path)

    while j >= 0:
        p = new_path[-1]
        c = new_path[-2]

        if p.right is c:
            if p.balance < -1:
                if c.balance > 0:
                    new_path = rotate_right_left(new_path)
                else:
                    new_path = rotate_left(new_path)
            elif p.balance == 0:
                break
        else:
            if p.balance > 1:
                if c.balance < 0:
                    new_path = rotate_left_right(new_path)
                else:
                    new_path = rotate_right(new_path)
            elif p.balance == 0:
                break

        if path:
            r = path.pop()
            if r.left is p:
                r.left = new_path[-1]
            else:
                r.right = new_path[-1]
            r.update()
            new_path.append(r)

        j -= 1

    new_path.reverse()

    path.extend(new_path)

    return path, 1


def rotate_left(path):
    p = path[-1]
    c = path[-2]
    q = path[-3]

    cl = c.left

    p.right = cl
    c.left = p

    p.update()
    c.update()

    if cl is q:
        path[-2] = p
        path[-1] = c
    else:
        path[-2] = c
        path.pop()

    return path


def rotate_right(path):
    p = path[-1]
    c = path[-2]
    q = path[-3]

    cr = c.right

    p.left = cr
    c.right = p

    p.update()
    c.update()

    if cr is q:
        path[-2] = p
        path[-1] = c
    else:
        path[-2] = c
        path.pop()

    return path


def rotate_right_left(path):
    p = path.pop()

    c = path[-1]

    path = rotate_right(path)

    if p.left is c:
        p.left = path[-1]
    else:
        p.right = path[-1]

    path.append(p)
    p.update()

    return rotate_left(path)


def rotate_left_right(path):
    p = path.pop()
    c = path[-1]

    path = rotate_left(path)

    if p.left is c:
        p.left = path[-1]
    else:
        p.right = path[-1]

    path.append(p)
    p.update()

    return rotate_right(path)
