import ds.binary_tree.iter as iter
import ds.binary_tree.find as find

from ds.binary_tree.node import Node


class BSTree:
    def __init__(self, root=None):
        self.root = root

    def __repr__(self):
        if self.root:
            return "Tree({})".format(self.root)
        return "Tree()"

    def __str__(self):
        return self.__repr__()

    def insert(self, data):
        child = Node(data)
        if not self.root:
            self.root = child
            return
        parent = self.root
        while 1:
            if parent.data == data:
                return
            elif data < parent.data:
                if parent.left:
                    parent = parent.left
                else:
                    parent.left = child
                    child.parent = parent
                    return
            else:
                if parent.right:
                    parent = parent.right
                else:
                    parent.right = child
                    child.parent = parent
                    return

    def delete(self, data):
        node = find.lookup(self.root, data)
        if node:
            target = node
            if node.degree() == 2:
                if succ := find.succ(node):
                    target = succ
            node.data = target.data
            child = target.left or target.right
            parent = target.parent
            if parent:
                if parent.left is target:
                    parent.left = child
                else:
                    parent.right = child
                if child:
                    child.parent = parent
            else:
                if child:
                    child.parent = None
                self.root = child

    def search(self, data):
        if node := find.lookup(self.root, data):
            return node.data

    def min(self):
        if node := find.min_leaf(self.root):
            return node.data

    def max(self):
        if node := find.max_leaf(self.root):
            return node.data

    def __iter__(self):
        return (node.data for node in iter.in_order(self.root))
