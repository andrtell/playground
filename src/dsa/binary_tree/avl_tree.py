import dsa.binary_tree.vary as vary

from dsa.binary_tree.bi_tree import BiTree, BiNode


class AVLNode(BiNode):
    def __init__(self, value):
        super().__init__(value)
        self.bf = 0


class AVLTree(BiTree):
    def insert(self, value):
        if not self.root:
            self.root = AVLNode(value)
            self.size = 1
            return

        path, updated = vary.insert([self.root], AVLNode(value))

        if not updated:
            return

        self.size += 1

        c = path.pop()

        while path:
            p = path.pop()

            if p.right is c:
                if p.bf < 0:
                    p.bf = 0
                    break

                if p.bf == 0:
                    p.bf = 1
                    c = p
                    continue

                if c.bf < 0:
                    n = rotate_right_left(p, c)
                else:
                    n = rotate_left(p, c)
            else:
                if p.bf > 0:
                    p.bf = 0
                    break

                if p.bf == 0:
                    p.bf = -1
                    c = p
                    continue

                if c.bf > 0:
                    n = rotate_left_right(p, c)
                else:
                    n = rotate_right(p, c)

            if path:
                pp = path[-1]
                if pp.left is p:
                    pp.left = n
                else:
                    pp.right = n
            else:
                self.root = n

            break

    def delete(self, value):
        if not self.root:
            return

        path, new_child, changed = vary.delete([self.root], value)

        if not changed:
            return

        self.size -= 1

        if not path:
            self.root = new_child
            return

        c = new_child

        while path:
            p = path.pop()

            if not (p.left or p.right):
                c = p
                c.bf = 0
                continue

            if p.left is c:
                if p.bf < 0:
                    c = p
                    c.bf = 0
                    continue

                if p.bf == 0:
                    p.bf = 1
                    break

                r = p.right
                bf = r.bf

                if bf < 0:
                    n = rotate_right_left(p, r)
                else:
                    n = rotate_left(p, r)
            else:
                if p.bf > 0:
                    c = p
                    c.bf = 0
                    continue

                if p.bf == 0:
                    p.bf = -1
                    break

                le = p.left
                bf = le.bf

                if bf > 0:
                    n = rotate_left_right(p, le)
                else:
                    n = rotate_right(p, le)

            c = n

            if path:
                pp = path[-1]
                if pp.left is p:
                    pp.left = n
                else:
                    pp.right = n
            else:
                self.root = n

            if bf == 0:
                break


# ----- ROTATE -------


def rotate_left(p, c):
    p.right = c.left
    c.left = p
    if c.bf == 0:
        p.bf = 1
        c.bf = -1
    else:
        p.bf = 0
        c.bf = 0
    return c


def rotate_right(p, c):
    p.left = c.right
    c.right = p
    if c.bf == 0:
        p.bf = -1
        c.bf = 1
    else:
        p.bf = 0
        c.bf = 0
    return c


def rotate_right_left(p, c):
    le = c.left
    c.left = le.right
    le.right = c
    p.right = le.left
    le.left = p
    if le.bf == 0:
        p.bf = 0
        c.bf = 0
    elif le.bf > 0:
        p.bf = -1
        c.bf = 0
    else:
        p.bf = 0
        c.bf = 1
    le.bf = 0
    return le


def rotate_left_right(p, c):
    ri = c.right
    c.right = ri.left
    ri.left = c
    p.left = ri.right
    ri.right = p
    if ri.bf == 0:
        p.bf = 0
        c.bf = 0
    elif ri.bf < 0:
        p.bf = 1
        c.bf = 0
    else:
        p.bf = 0
        c.bf = -1
    ri.bf = 0
    return ri
