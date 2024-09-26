class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1

    def update_height(self):
        h = max(
            self.left and self.left.height or 0,
            self.right and self.right.height or 0,
        )
        self.height = 1 + h

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
