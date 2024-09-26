class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 0

    def update_height(self):
        h = 0
        if self.left:
            h = max(h, self.left.height)
        if self.right:
            h = max(h, self.right.height)
        self.height = h + 1

    def __repr__(self):
        s = []

        s.append(f"{self.data}, height={self.height}")

        if self.left:
            s.append(f"left={self.left}")

        if self.right:
            s.append(f"right={self.right}")

        return "Node(" + ", ".join(s) + ")"

    def __str__(self):
        return self.__repr__()
