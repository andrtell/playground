import ds.binary_tree.iter as iter
import ds.binary_tree.find as find

import ds.binary_tree.bst as bst
import ds.binary_tree.avl as avl

from ds.binary_tree.node import Node


class Tree:
    def __init__(self, strategy=avl):
        self.strategy = strategy
        self.root = []
        self.size = 0

    def __len__(self):
        return self.size

    def insert(self, data):
        path, count = find.lookup(self.root, data)

        if count > 0:
            return

        path, count = self.strategy.insert(path, Node(data))

        self.root = path[:1]
        self.size += count

    def delete(self, data):
        path, count = find.lookup([self.root], data)

        if count < 1:
            return

        path, count = self.strategy.delete(path)

        self.root = path[0:1]
        self.size -= count

    def has(self, data):
        _, count = find.lookup(self.root[:], data)
        return bool(count)

    def __contains__(self, data):
        return self.has(data)

    def min(self):
        if self.root:
            return find.min_leaf(self.root[:])[-1].data

    def max(self):
        if self.root:
            return find.max_leaf(self.root[:])[-1].data

    def __iter__(self):
        return (node.data for node in iter.in_order(self.root))

    def __repr__(self):
        if self.root:
            return "Tree({})".format(self.root)
        return "Tree()"

    def __str__(self):
        return self.__repr__()
