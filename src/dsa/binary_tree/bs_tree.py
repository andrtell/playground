import dsa.binary_tree.vary as vary

from dsa.binary_tree.bi_tree import BiTree, BiNode


class BSNode(BiNode):
    pass


class BSTree(BiTree):
    def insert(self, value):
        if self.root:
            _, updated = vary.insert([self.root], BSNode(value))
            if updated:
                self.size += 1
        else:
            self.root = BSNode(value)
            self.size = 1

    def delete(self, value):
        if self.root:
            path, updated = vary.delete([self.root], value)
            if not updated:
                return
            self.root = path and path[0] or None
            self.size -= 1
