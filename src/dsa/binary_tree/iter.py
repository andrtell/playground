import collections
import dataclasses

from dsa.binary_tree.node_info import NodeInfo

def in_order(root, reverse=False):
    if root:
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


def pre_order(root, reverse=False):
    if root:
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


def post_order(root, reverse=False):
    if root:
        stack = [(root, 0, 1)]
        order = []

        while stack:
            node, side, depth = stack.pop()

            order.append((node, NodeInfo(side=side, depth=depth)))

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

        while order:
            yield order.pop()


def level_order(root):
    if root:
        count = 1
        level = collections.deque([(root, 0, 0)])
        while count:
            while count > 0:
                count -= 1

                node, side, depth = level.popleft()

                yield (node, NodeInfo(side=side, depth=depth))

                if node.left:
                    level.append((node.left, -1, depth + 1))

                if node.right:
                    level.append((node.right, 1, depth + 1))

            count = len(level)
