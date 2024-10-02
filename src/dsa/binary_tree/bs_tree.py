import dsa.binary_tree.vary as vary

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
            _, changed = vary.insert([self.root], BSNode(value))

            if changed:
                self.size += 1
        else:
            self.root = BSNode(value)
            self.size = 1

    def delete(self, value):
        if self.root:
            path, new_child, changed = vary.delete([self.root], value)

            if not changed:
                return

            self.root = path and path[0] or new_child
            self.size -= 1
