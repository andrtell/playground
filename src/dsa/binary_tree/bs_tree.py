from dsa.binary_tree.path import Path

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
            inserted, _ = BSOp.insert(self.root, BSNode(value))
            if inserted:
                self.size += 1
        else:
            self.root = BSNode(value)
            self.size = 1

    def delete(self, value):
        if self.root:
            deleted, path, new_child = BSOp.delete(self.root, value)
            if deleted:
                self.size -= 1
                if path:
                    self.root = path[0]
                else:
                    self.root = new_child

class BSOp:
    @classmethod
    def insert(cls, root, node):
        if not root:
            raise Exception("Can't call insert if root is None.")

        found, path = Path.find(root, node.value)

        if found:
            return False, path

        parent = path[-1]

        if node.value < parent.value:
            parent.left = node
        else:
            parent.right = node

        path.append(node)

        return True, path

    @classmethod
    def delete(cls, root, value):
        if not root:
            raise Exception("Can't call delete if root is None.")

        found, path = Path.find(root, value)

        if not found:
            return False, [], None

        node = remo = path[-1]

        if node.left and node.right:
            path.extend(Path.min_leaf(node.right))
            remo = path[-1]
            node.value = remo.value

        path.pop()

        new_child = remo.left or remo.right

        if path:
            parent = path[-1]

            if parent.left is remo:
                parent.left = new_child
            else:
                parent.right = new_child

        return True, path, new_child
