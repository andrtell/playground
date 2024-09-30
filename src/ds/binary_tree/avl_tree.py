import ds.binary_tree.vary as vary

from ds.binary_tree.bi_tree import BiTree, BiNode


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
                if p.bf > 0:
                    if c.bf < 0:
                        n = rotate_right_left(p, c)
                    else:
                        n = rotate_left(p, c)
                else:
                    if p.bf < 0:
                        p.bf = 0
                        return
                    else:
                        p.bf += 1
                        c = p
                        continue
            else:
                if p.bf < 0:
                    if c.bf > 0:
                        n = rotate_left_right(p, c)
                    else:
                        n = rotate_right(p, c)
                else:
                    if p.bf > 0:
                        p.bf = 0
                        return
                    else:
                        p.bf -= 1
                        c = p
                        continue

            if path:
                r = path[-1]
                if r.left is p:
                    r.left = n
                else:
                    r.right = n
            else:
                self.root = n

            return

    def delete(self, value):
        if not self.root:
            return

        path, updated = vary.delete([self.root], value)

        if not updated:
            return

        if not path:
            self.root = None
            self.size = 0
            return

        if len(path) < 2:
            self.root = path[0]
            self.size = 1
            self.root.bf = 0
            return

        self.size -= 1

        c = path.pop()

        while path:
            p = path.pop()

            if p.left is c:
                if p.bf > 0:
                    c_r = p.right
                    b = c_r.bf
                    if b < 0:
                        n = rotate_right_left(p, c_r)
                    else:
                        n = rotate_left(p, c_r)
                else:
                    if p.bf == 0:
                        p.bf += 1
                        return
                    else:
                        p.bf = 0
                        c = p
                        continue
            else:
                if p.bf < 0:
                    c_l = p.left
                    b = c_l.bf
                    if b > 0:
                        n = rotate_left_right(p, c_l)
                    else:
                        n = rotate_right(p, c_l)
                else:
                    if p.bf == 0:
                        p.bf -= 1
                        return
                    else:
                        p.bf = 0
                        c = p
                        continue

            if path:
                r = path[-1]
                if r.left is p:
                    r.left = n
                else:
                    r.right = n
            else:
                self.root = n

            if b == 0:
                return


# ----- ROTATE -------


def rotate_left(p, c):
    p.right = c.left
    c.left = p
    if c.bf == 0:
        p.bf += 1
        c.bf -= 1
    else:
        p.bf = 0
        c.bf = 0
    return c


def rotate_right(p, c):
    p.left = c.right
    c.right = p
    if c.bf == 0:
        p.bf -= 1
        c.bf += 1
    else:
        p.bf = 0
        c.bf = 0
    return c


def rotate_right_left(p, c):
    q = c.left

    c.left = q.right
    q.right = c

    p.right = q.left
    q.left = p

    if q.bf == 0:
        p.bf = 0
        c.bf = 0
    elif q.bf > 0:
        p.bf -= 1
        c.bf = 0
    else:
        p.bf = 0
        c.bf += 1

    q.bf = 0

    return q


def rotate_left_right(p, c):
    q = c.right

    c.right = q.left
    q.left = c

    p.left = q.right
    q.right = p

    if q.bf == 0:
        p.bf = 0
        c.bf = 0
    elif q.bf < 0:
        p.bf += 1
        c.bf = 0
    else:
        p.bf = 0
        c.bf -= 1

    q.bf = 0

    return q
