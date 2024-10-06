from dsa.binary_tree.iter import Iter


class Query:
    @classmethod
    def height(cls, node):
        height = 0
        for _, path in Iter.pre_order(node):
            height = max(height, len(path))
        return height

    @classmethod
    def balance(cls, node):
        if node:
            return cls.height(node.right) - cls.height(node.left)
        else:
            return 0
