import collections


def in_order(root):
    if root:
        node = root
        depth = 1
        stack = []
        while True:
            if node:
                stack.append((node, depth))
                depth += 1
                node = node.left
            elif stack:
                node, depth = stack.pop()
                yield node, depth
                node = node.right
            else:
                break


def pre_order(root):
    if root:
        node = root
        depth = 1
        stack = []
        while True:
            if node:
                yield (node, depth)
                depth += 1
                stack.append((node, depth))
                node = node.left
            elif stack:
                parent, depth = stack.pop()
                node = parent.right
            else:
                break


def post_order(root):
    if root:
        stack = [(root, 1)]
        order = []
        while stack:
            node, depth = stack.pop()
            order.append(node)
            if node.left:
                stack.append((node.left, depth + 1))
            if node.right:
                stack.append((node.right, depth + 1))
        while order:
            yield order.pop()


def level_order(root):
    if root:
        depth = 1
        count = 1
        que = collections.deque([root])
        while count > 0:
            while count > 0:
                count -= 1
                node = que.popleft()
                yield (node, depth)
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
            count = len(que)
            depth += 1
