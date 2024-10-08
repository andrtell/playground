from typing import Optional
from dsa.binary_tree.iter import Iter
from dsa.binary_tree.path import Path
from dsa.binary_tree.format import Format


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left: Optional[Node] = left
        self.right: Optional[Node] = right

    def __repr__(self):
        return f"Node(value={repr(self.value)}, left={repr(self.left)}, right={repr(self.right)})"

    def __str__(self):
        return "\n".join(list(Format.horizontal_2(self)))


class Tree:
    def __init__(self, root=None):
        self.root: Optional[Node] = root
        self.size = 0

    def insert(self, value):
        pass

    def delete(self, value):
        pass

    def find(self, value):
        if self.root:
            found, path = Path.find(self.root, value)
            if found:
                return path[-1].value

    def __contains__(self, value):
        return bool(self.find(value))

    def min(self):
        if self.root:
            path = Path.min_leaf(self.root)
            return path[-1].value

    def max(self):
        if self.root:
            path = Path.max_leaf(self.root)
            return path[-1].value

    def __len__(self):
        return self.size

    def __bool__(self):
        return self.size > 0

    def __iter__(self):
        return (path[-1].value for path in Iter.in_order(self.root))

    def __repr__(self):
        if self.root:
            return f"Tree({repr(self.root)})"

        return "Tree()"

    def __str__(self):
        if self.root:
            return str(self.root)
        else:
            return ""
