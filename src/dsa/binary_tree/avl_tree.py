from dsa.binary_tree.tree import Tree, Node
from dsa.binary_tree.bs_tree import BSOp


def avltree(iter):
    tree = AVLTree()
    for value in iter:
        tree.insert(value)
    return tree


class AVLNode(Node):
    def __init__(self, value):
        super().__init__(value)
        self.bf = 0

    @classmethod
    def rotate_left(cls, par):
        chi = par.right
        par.right = chi.left
        chi.left = par

        if chi.bf == 0:
            par.bf = 1
            chi.bf = -1
        else:
            par.bf = 0
            chi.bf = 0

        return chi

    @classmethod
    def rotate_right(cls, par):
        chi = par.left
        par.left = chi.right
        chi.right = par

        if chi.bf == 0:
            par.bf = -1
            chi.bf = 1
        else:
            par.bf = 0
            chi.bf = 0

        return chi

    @classmethod
    def rotate_right_left(cls, par):
        chi = par.right
        lef = chi.left
        chi.left = lef.right
        lef.right = chi
        par.right = lef.left
        lef.left = par

        if lef.bf == 0:
            par.bf = 0
            chi.bf = 0
        elif lef.bf > 0:
            par.bf = -1
            chi.bf = 0
        else:
            par.bf = 0
            chi.bf = 1

        lef.bf = 0

        return lef

    @classmethod
    def rotate_left_right(cls, par):
        chi = par.left
        rig = chi.right
        chi.right = rig.left
        rig.left = chi
        par.left = rig.right
        rig.right = par

        if rig.bf == 0:
            par.bf = 0
            chi.bf = 0
        elif rig.bf < 0:
            par.bf = 1
            chi.bf = 0
        else:
            par.bf = 0
            chi.bf = -1

        rig.bf = 0

        return rig


class AVLTree(Tree):
    def insert(self, value):
        if not self.root:
            self.root = AVLNode(value)
            self.size = 1
            return

        did_insert, path = BSOp.insert(self.root, AVLNode(value))

        if not did_insert:
            return

        self.size += 1

        chi = path.pop()

        while path:
            par = path.pop()

            if par.right is chi:
                if par.bf < 0:
                    par.bf = 0
                    break

                if par.bf == 0:
                    par.bf = 1
                    chi = par
                    continue

                if chi.bf < 0:
                    new_par = AVLNode.rotate_right_left(par)
                else:
                    new_par = AVLNode.rotate_left(par)
            else:
                if par.bf > 0:
                    par.bf = 0
                    break

                if par.bf == 0:
                    par.bf = -1
                    chi = par
                    continue

                if chi.bf > 0:
                    new_par = AVLNode.rotate_left_right(par)
                else:
                    new_par = AVLNode.rotate_right(par)

            if path:
                if path[-1].left is par:
                    path[-1].left = new_par
                else:
                    path[-1].right = new_par
            else:
                self.root = new_par

            break

    def delete(self, value):
        if not self.root:
            return

        did_delete, path, new_chi = BSOp.delete(self.root, value)

        if not did_delete:
            return

        self.size -= 1

        if not path:
            self.root = new_chi
            return

        chi = new_chi

        while path:
            par = path.pop()

            if not (par.left or par.right):
                chi = par
                chi.bf = 0
                continue

            if par.left is chi:
                if par.bf < 0:
                    chi = par
                    chi.bf = 0
                    continue

                if par.bf == 0:
                    par.bf = 1
                    break

                bf = par.right.bf

                if bf < 0:
                    new_par = AVLNode.rotate_right_left(par)
                else:
                    new_par = AVLNode.rotate_left(par)
            else:
                if par.bf > 0:
                    chi = par
                    chi.bf = 0
                    continue

                if par.bf == 0:
                    par.bf = -1
                    break

                bf = par.left.bf

                if bf > 0:
                    new_par = AVLNode.rotate_left_right(par)
                else:
                    new_par = AVLNode.rotate_right(par)

            chi = new_par

            if path:
                if path[-1].left is par:
                    path[-1].left = new_par
                else:
                    path[-1].right = new_par
            else:
                self.root = new_par

            if bf == 0:
                break
