import dsa.binary_tree.alter as alter

from dsa.binary_tree.bi_tree import BiTree, BiNode


def avltree(iter):
    tree = AVLTree()
    for value in iter:
        tree.insert(value)
    return tree


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

        spine, changed = alter.insert([self.root], AVLNode(value))

        if not changed:
            return

        self.size += 1

        c = spine.pop()

        while spine:
            p = spine.pop()

            if p.right is c:
                if p.bf < 0:
                    p.bf = 0
                    break

                if p.bf == 0:
                    p.bf = 1
                    c = p
                    continue

                if c.bf < 0:
                    n = rotate_right_left(p)
                else:
                    n = rotate_left(p)
            else:
                if p.bf > 0:
                    p.bf = 0
                    break

                if p.bf == 0:
                    p.bf = -1
                    c = p
                    continue

                if c.bf > 0:
                    n = rotate_left_right(p)
                else:
                    n = rotate_right(p)

            if spine:
                pp = spine[-1]
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

        spine, new_child, changed = alter.delete([self.root], value)

        if not changed:
            return

        self.size -= 1

        if not spine:
            self.root = new_child
            return

        c = new_child

        while spine:
            p = spine.pop()

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

                bf = p.right.bf

                if bf < 0:
                    n = rotate_right_left(p)
                else:
                    n = rotate_left(p)
            else:
                if p.bf > 0:
                    c = p
                    c.bf = 0
                    continue

                if p.bf == 0:
                    p.bf = -1
                    break

                bf = p.left.bf

                if bf > 0:
                    n = rotate_left_right(p)
                else:
                    n = rotate_right(p)

            c = n

            if spine:
                pp = spine[-1]
                if pp.left is p:
                    pp.left = n
                else:
                    pp.right = n
            else:
                self.root = n

            if bf == 0:
                break


# ----- ROTATE -------


def rotate_left(p):
    c = p.right
    p.right = c.left
    c.left = p
    if c.bf == 0:
        p.bf = 1
        c.bf = -1
    else:
        p.bf = 0
        c.bf = 0
    return c


def rotate_right(p):
    c = p.left
    p.left = c.right
    c.right = p
    if c.bf == 0:
        p.bf = -1
        c.bf = 1
    else:
        p.bf = 0
        c.bf = 0
    return c


def rotate_right_left(p):
    c = p.right
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


def rotate_left_right(p):
    c = p.left
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
