from dataclasses import dataclass


@dataclass
class NodeInfo:
    side: int
    depth: int

    def is_root(self):
        return self.side == 0

    def is_left(self):
        return self.side == -1

    def is_right(self):
        return self.side == 1
