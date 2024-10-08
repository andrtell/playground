from dsa.binary_tree.path import Path
from dsa.binary_tree.tree import Tree, Node


def bstree(iter):
    tree = BSTree()
    for value in iter:
        tree.insert(value)
    return tree


class BSTree(Tree):
    def insert(self, value):
        if self.root:
            did_insert, _ = BSOp.insert(self.root, Node(value))
            if did_insert:
                self.size += 1
        else:
            self.root = Node(value)
            self.size = 1

    def delete(self, value):
        if self.root:
            did_delete, path, new_chi = BSOp.delete(self.root, value)
            if did_delete:
                self.size -= 1
                if path:
                    self.root = path[0]
                else:
                    self.root = new_chi


class BSOp:
    @classmethod
    def insert(cls, root, new_chi):
        if not root:
            raise Exception("Can't call insert if root is None.")

        found, path = Path.find(root, new_chi.value)

        if found:
            return False, path

        par = path[-1]

        if new_chi.value < par.value:
            par.left = new_chi
        else:
            par.right = new_chi

        path.append(new_chi)

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

        new_chi = remo.left or remo.right

        if path:
            if path[-1].left is remo:
                path[-1].left = new_chi
            else:
                path[-1].right = new_chi

        return True, path, new_chi
