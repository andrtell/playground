from typing import Optional

import dsa.binary_tree.iter as iter

from  dsa.binary_tree.spine import Spine


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
            spine = Spine(self.root)
            if spine.search(value):
                return spine.peek().value

    def __contains__(self, value):
        return bool(self.find(value))

    def min(self):
        if self.root:
            spine = Spine(self.root)
            if spine.min_leaf():
                return spine.peek().value

    def max(self):
        if self.root:
            spine = Spine(self.root)
            if spine.max_leaf():
                return spine.peek().value

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
