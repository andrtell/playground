import ds.binary_tree.iter as iter
import ds.binary_tree.find as find

import ds.binary_tree.bst as bst

from ds.binary_tree.node import Node


class Tree:
    def __init__(self, strategy=bst):
        self.root: Node | None = None
        self.size = 0
        self.strategy = strategy

    def __repr__(self):
        if self.root:
            return "Tree({})".format(self.root)
        return "Tree()"

    def __str__(self):
        return self.__repr__()

    def __len__(self):
        return self.size

    def insert(self, data):
        self.root, count = self.strategy.insert(self.root, Node(data))
        self.size += count

    def delete(self, data):
        node, path = find.node(self.root, data)
        self.root, count = self.strategy.delete(node, path)
        self.size -= count

    def has(self, data):
        node, _ = find.node(self.root, data)
        return node and node.data

    def __contains__(self, data):
        return self.has(data)

    def min(self):
        node, _ = find.min_leaf(self.root)
        return node and node.data

    def max(self):
        node, _ = find.max_leaf(self.root)
        return node and node.data

    def __iter__(self):
        return (node.data for node in iter.in_order(self.root))
