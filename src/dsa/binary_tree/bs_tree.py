import dsa.binary_tree.modify as modify

from dsa.binary_tree.bi_tree import BiTree, BiNode


def bstree(iter):
    tree = BSTree()
    for value in iter:
        tree.insert(value)
    return tree


class BSNode(BiNode):
    pass


class BSTree(BiTree):
    def insert(self, value):
        if self.root:
            _, changed = modify.insert([self.root], BSNode(value))

            if changed:
                self.size += 1
        else:
            self.root = BSNode(value)
            self.size = 1

    def delete(self, value):
        if self.root:
            spine, new_child, changed = modify.delete([self.root], value)

            if not changed:
                return

            self.root = spine and spine[0] or new_child
            self.size -= 1
