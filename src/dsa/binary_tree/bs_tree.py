from dsa.binary_tree.spine import Spine

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
            spine = Spine(self.root)
            changed = spine.insert(BSNode(value))
            if changed:
                self.size += 1
        else:
            self.root = BSNode(value)
            self.size = 1

    def delete(self, value):
        if self.root:
            spine = Spine(self.root)
            changed, new_child = spine.delete(value)
            if changed:
                self.size -= 1
                if spine:
                    self.root = spine.first()
                else:
                    self.root = new_child
