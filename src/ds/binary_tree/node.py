class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1
        self.balance = 0

    def update(self):
        lh = self.left and self.left.height or 0
        rh = self.right and self.right.height or 0
        self.height = 1 + max(lh, rh)
        self.balance = lh - rh

    def __repr__(self):
        s = []
        s.append(f"{self.data}, height={self.height}, balance={self.balance}")
        return "Node(" + ", ".join(s) + ")"

    def __str__(self):
        return self.__repr__()
