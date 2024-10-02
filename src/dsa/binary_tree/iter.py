import collections


def in_order(root):
    if root:
        stack, node = [], root
        while True:
            if node:
                stack.append(node)
                node = node.left
            elif stack:
                node = stack.pop()
                yield node
                node = node.right
            else:
                break


def pre_order(root):
    if root:
        lvl = 0
        stack, node = [], root
        while True:
            if node:
                yield (node, lvl)
                stack.append((node, lvl + 1))
                node = node.left
                lvl += 1
            elif stack:
                parent, lvl = stack.pop()
                node = parent.right
            else:
                break


def post_order(root):
    if root:
        stack, order = [root], []
        while stack:
            node = stack.pop()
            order.append(node)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        while order:
            yield order.pop()


def level_order(root):
    if root:
        items = 1
        level = 1
        que = collections.deque([root])
        while items > 0:
            while items > 0:
                items -= 1
                node = que.popleft()
                yield (node, level)
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
            items = len(que)
            level += 1
