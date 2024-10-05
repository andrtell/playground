import collections
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


class Iter:
    @classmethod
    def pre_order(cls, root):
        if not root:
            return

        cur = root
        his = []
        pth = []

        while True:
            if cur:
                yield cur, pth
                his.append(cur)
                pth.append(cur)
                cur = cur.left
            elif his:
                par = his.pop()
                cur = par.right
                while pth and par is not pth[-1]:
                    pth.pop()
            else:
                break

    @classmethod
    def in_order(cls, root):
        if not root:
            return

        cur = root
        his = []
        pth = []

        while True:
            if cur:
                his.append(cur)
                pth.append(cur)
                cur = cur.left
            elif his:
                par = his.pop()
                cur = par.right
                while pth and pth[-1] is not par:
                    pth.pop()
                if pth:
                    pth.pop()
                yield par, pth
                pth.append(par)
            else:
                break

    @classmethod
    def post_order(cls, root):
        if not root:
            return

        cur = root
        his = []
        pth = []

        while True:
            if cur:
                his.append(cur)
                pth.append(cur)
                cur = cur.left
            elif his:
                par = his.pop()
                cur = par.right
                while pth and pth[-1] is not par:
                    yield pth.pop(), pth
            else:
                break

        while pth:
            yield pth.pop(), pth

    @classmethod
    def level_order(cls, root):
        if not root:
            return

        count = 1
        nodes = collections.deque([(root, 0, 0)])

        while count:
            while count > 0:
                count -= 1

                node, side, depth = nodes.popleft()

                yield (node, NodeInfo(side=side, depth=depth))

                if node.left:
                    nodes.append((node.left, -1, depth + 1))

                if node.right:
                    nodes.append((node.right, 1, depth + 1))

            count = len(nodes)
