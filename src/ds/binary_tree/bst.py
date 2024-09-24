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

        if self.root:
            parent = self.root
            while True:
                if data < parent.data:
                    if not parent.left:
                        parent.set_left(child)
                        break
                    else:
                        parent = parent.left
                else:
                    if not parent.right:
                        parent.set_right(child)
                        break
                    else:
                        parent = parent.right
        else:
            self.root = child

        return child

    def delete(self, data):
        for node in Node.find(self.root, data):
            rem = node

            if node.degree() == 2:
                for succ in Node.next(node):
                    rem = succ

            parent = rem.parent

            child = rem.first_child()

            if parent:
                if parent.left is rem:
                    parent.set_left(child)
                else:
                    parent.set_right(child)
            else:
                self.root = child

            node.data = rem.data

            return rem

    def search(self, data):
        for node in Node.find(self.root, data):
            return node.data

    def min(self):
        for node in Node.min_leaf(self.root):
            return node.data

    def max(self):
        for node in Node.max_leaf(self.root):
            return node.data

    def info(self):
        return Node.info(self.root)

    def __iter__(self):
        for node in Node.in_order(self.root):
            yield node.data
