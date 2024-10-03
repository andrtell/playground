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
    def in_order(cls, root, reverse=False):
        if not root:
            return

        node = root
        side = 0
        depth = -1
        spine = []

        while True:
            if node:
                depth += 1

                spine.append((node, side, depth))

                if reverse:
                    side = 1
                    node = node.right
                else:
                    side = -1
                    node = node.left
            elif spine:
                node, side, depth = spine.pop()

                yield node, NodeInfo(side=side, depth=depth)

                if reverse:
                    side = -1
                    node = node.left
                else:
                    side = 1
                    node = node.right
            else:
                break

    @classmethod
    def pre_order(cls, root, reverse=False):
        if not root:
            return

        node = root
        side = 0
        depth = -1
        spine = []

        while True:
            if node:
                depth += 1

                yield (node, NodeInfo(side=side, depth=depth))

                spine.append((node, side, depth))

                if reverse:
                    side = 1
                    node = node.right
                else:
                    side = -1
                    node = node.left
            elif spine:
                node, _, depth = spine.pop()

                if reverse:
                    side = -1
                    node = node.left
                else:
                    side = 1
                    node = node.right
            else:
                break

    @classmethod
    def post_order(cls, root, reverse=False):
        if not root:
            return

        stack = [(root, 0, 1)]
        nodes = []

        while stack:
            node, side, depth = stack.pop()

            nodes.append((node, NodeInfo(side=side, depth=depth)))

            if reverse:
                if node.right:
                    stack.append((node.right, 1, depth + 1))

                if node.left:
                    stack.append((node.left, -1, depth + 1))
            else:
                if node.left:
                    stack.append((node.left, -1, depth + 1))

                if node.right:
                    stack.append((node.right, 1, depth + 1))

        while nodes:
            yield nodes.pop()

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
