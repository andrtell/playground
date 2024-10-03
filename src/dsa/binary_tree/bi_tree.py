from typing import Optional

import dsa.binary_tree.iter as iter
import dsa.binary_tree.path as path


class BiNode:
    def __init__(self, value):
        self.value = value
        self.left: Optional[BiNode] = None
        self.right: Optional[BiNode] = None

    def __repr__(self):
        return f"Node({self.value})"

    def __str__(self):
        return self.__repr__()


class BiTree:
    def __init__(self, root=None):
        self.root = root
        self.size = 0

    def insert(self, value):
        pass

    def delete(self, value):
        pass

    def find(self, value):
        if self.root:
            spine, found = path.find([self.root], value)

            if found:
                return spine[-1].value

    def __contains__(self, value):
        return bool(self.find(value))

    def min(self):
        if self.root:
            spine = path.min_leaf([self.root])

            if path:
                return spine[-1].value

    def max(self):
        if self.root:
            spine = path.max_leaf([self.root])

            if path:
                return spine[-1].value

    def left(self):
        return type(self)(self.root and self.root.left or None)

    def right(self):
        return type(self)(self.root and self.root.right or None)

    def __len__(self):
        return self.size

    def __iter__(self):
        return (node.value for node, _ in iter.in_order(self.root))

    def __repr__(self):
        if self.root:
            return f"Tree({self.root})"

        return "Tree()"

    def __str__(self):
        str = ""
        for node, info in iter.pre_order(self.root):
            str = str + ("  " * info.depth) + node.__str__() + "\n"
        return str
