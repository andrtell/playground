import dsa.binary_tree.iter as iter
import dsa.binary_tree.find as find

from typing import Optional


class BiNode:
    def __init__(self, value):
        self.value = value
        self.left: Optional[BiNode] = None
        self.right: Optional[BiNode] = None

    def update(self):
        pass

    def __repr__(self):
        return f"Node({self.value})"

    def __str__(self):
        return self.__repr__()


class BiTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def __len__(self):
        return self.size

    def insert(self, value):
        pass

    def insert_from(self, iter):
        for value in iter:
            self.insert(value)

    def delete(self, value):
        pass

    def find(self, data):
        if self.root:
            path, found = find.lookup([self.root], data)
            if found:
                return path[-1].value

    def __contains__(self, data):
        return bool(self.find(data))

    def min(self):
        if self.root:
            path = find.min_leaf([self.root])
            if path:
                return path[-1].value

    def max(self):
        if self.root:
            path = find.max_leaf([self.root])
            if path:
                return path[-1].value

    def __iter__(self):
        return (node.value for node in iter.in_order(self.root))

    def __repr__(self):
        if self.root:
            return f"Tree({self.root})"
        return "Tree()"

    def __str__(self):
        return self.__repr__()
