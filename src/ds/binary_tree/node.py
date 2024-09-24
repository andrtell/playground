class Node:
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.left = None
        self.right = None

    def __repr__(self):
        s = []

        s.append(f"{self.data}")

        if self.left:
            s.append(f"left={self.left}")

        if self.right:
            s.append(f"right={self.right}")

        return "Node(" + ", ".join(s) + ")"

    def __str__(self):
        return self.__repr__()

    def is_child(self):
        return bool(self.parent)

    def is_leaf(self):
        return not (self.left or self.right)

    def is_left(self):
        return self.parent and self is self.parent.left

    def is_right(self):
        return self.parent and self is self.parent.right

    def degree(self):
        return (self.left and 1 or 0) + (self.right and 1 or 0)
