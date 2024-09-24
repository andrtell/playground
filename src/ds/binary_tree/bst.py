import collections
from dataclasses import dataclass


class BSTree:
    def __init__(self, root=None):
        self.root = root

    def __repr__(self):
        if self.root:
            return "Tree({})".format(self.root)
        return "Tree()"

    def __str__(self):
        return self.__repr__()

    def insert(self, data):
        child = BSNode(data)
        if self.root:
            BSNode.insert(self.root, child)
        else:
            self.root = child

    def delete(self, data):
        for node in BSNode.find(self.root, data):
            self.root = BSNode.delete(self.root, node)

    def search(self, data):
        for node in BSNode.find(self.root, data):
            return node.data

    def min(self):
        for node in BSNode.min_leaf(self.root):
            return node.data

    def max(self):
        for node in BSNode.max_leaf(self.root):
            return node.data

    def info(self):
        return BSNode.info(self.root)

    def __iter__(self):
        for node in BSNode.in_order(self.root):
            yield node.data


class BSNode:
    def __init__(self, data, parent=None, left=None, right=None):
        self.data = data
        self.parent = parent
        self.set_left(left)
        self.set_right(right)

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

    def is_child(self):
        return bool(self.parent)

    def is_leaf(self):
        return not (self.left or self.right)

    def is_left(self):
        return self.parent and self is self.parent.left

    def is_right(self):
        return self.parent and self is self.parent.right

    def degree(self):
        return (self.left and 1 or 0) + (self.right and 1 or 0)

    def set_left(self, child):
        self.left = child
        if child:
            child.parent = self

    def set_right(self, child):
        self.right = child
        if child:
            child.parent = self

    def first_child(self):
        if self.left:
            return self.left

        return self.right

    def balance_factor(self):
        return BSNode.height(self.right) - BSNode.height(self.left)

    @classmethod
    def insert(cls, root, node):
        if root:
            parent = root
            while True:
                if node.data < parent.data:
                    if not parent.left:
                        parent.set_left(node)
                        break
                    else:
                        parent = parent.left
                else:
                    if not parent.right:
                        parent.set_right(node)
                        break
                    else:
                        parent = parent.right

    @classmethod
    def delete(cls, root, node):
        rem = node

        if node.degree() == 2:
            for succ in BSNode.next(node):
                rem = succ

        if node is not rem:
            node.data = rem.data

        child = rem.first_child()

        if rem.parent:
            if rem.parent.left is rem:
                rem.parent.set_left(child)
            else:
                rem.parent.set_right(child)

            return root
        else:
            if child:
                child.parent = None

            return child

    @classmethod
    def rotate_left(cls, root):
        right_child = root.right
        if right_child:
            root.set_right(right_child.left)
            right_child.set_left(root)

    @classmethod
    def rotate_right(cls, root):
        left_child = root.left
        if left_child:
            root.set_left(left_child.right)
            left_child.set_right(root)

    @classmethod
    def height(cls, root):
        if not root:
            return 0
        items = 1
        level = 1
        que = collections.deque([root])
        while items > 0:
            while items > 0:
                items -= 1
                node = que.popleft()
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
            items = len(que)
            level += 1
        return level

    @classmethod
    def next(cls, node):
        if node and node.right:
            yield from cls.min_leaf(node.right)
        else:
            while node and node.is_right():
                node = node.parent

            if node and node.parent:
                yield node.parent

    @classmethod
    def prev(cls, node):
        if node and node.left:
            yield from cls.max_leaf(node.left)
        else:
            while node and node.is_left():
                node = node.parent

            if node and node.parent:
                yield node.parent

    @classmethod
    def find(cls, root, data):
        if root:
            node = root
            while node and node.data != data:
                if data < node.data:
                    node = node.left
                else:
                    node = node.right
            yield node

    @classmethod
    def min_leaf(cls, root):
        if root:
            node = root
            while node.left:
                node = node.left
            yield node

    @classmethod
    def max_leaf(cls, root):
        if root:
            node = root
            while node.right:
                node = node.right
            yield node

    @classmethod
    def in_order(cls, root):
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

    @classmethod
    def pre_order(cls, root):
        if root:
            stack, node = [], root
            while True:
                if node:
                    yield node
                    stack.append(node)
                    node = node.left
                elif stack:
                    node = stack.pop().right
                else:
                    break

    @classmethod
    def post_order(cls, root):
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

    @classmethod
    def level_order(cls, root):
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

    @classmethod
    def info(cls, root):
        level = 0
        size = 0
        leaf_count = 0
        is_full = True
        is_complete = True

        seen_not_filled = False

        for node, lvl in cls.level_order(root):
            size += 1
            degree = node.degree()
            if degree == 0:
                leaf_count += 1
            if degree > 0 and seen_not_filled:
                is_complete = False
            if degree == 1:
                is_full = False
                if node.right:
                    is_complete = False
            if degree < 2:
                seen_not_filled = True
            level = lvl

        return NodeInfo(
            size=size,
            height=level,
            leaf_count=leaf_count,
            is_full=is_full,
            is_complete=is_complete,
        )


@dataclass
class NodeInfo:
    height: int = 0
    size: int = 0
    leaf_count: int = 0
    is_full: bool = True
    is_complete: bool = True
