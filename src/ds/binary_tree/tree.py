import ds.binary_tree.iter as iter
import ds.binary_tree.find as find

import ds.binary_tree.bst as bst


class Tree:
    def __init__(self, strategy=bst):
        self.strategy = strategy
        self.root = []
        self.size = 0

    def __len__(self):
        return self.size

    def insert(self, data):
        path, count = self.strategy.insert(self.root, data)
        self.root = path[0:1]
        self.size += count

    def delete(self, data):
        path, count = self.strategy.delete(self.root, data)
        self.root = path[0:1]
        self.size -= count

    def has(self, data):
        path, count = find.lookup(self.root, data)
        if count:
            return path[-1].data

    def __contains__(self, data):
        return bool(self.has(data))

    def min(self):
        if self.root:
            return find.min_leaf(self.root)[-1].data

    def max(self):
        if self.root:
            return find.max_leaf(self.root)[-1].data

    def __iter__(self):
        return (node.data for node in iter.in_order(self.root))

    def __repr__(self):
        if self.root:
            return "Tree({})".format(self.root)
        return "Tree()"

    def __str__(self):
        return self.__repr__()
