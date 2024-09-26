class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 0

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
