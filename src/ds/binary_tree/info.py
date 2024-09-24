import collections
from dataclasses import dataclass
import ds.binary_tree.iter as iter


def height(root):
    level = 1
    parents = 1
    que = collections.deque([root])
    while parents > 0:
        while parents > 0:
            parents -= 1
            node = que.popleft()
            if node.left:
                que.append(node.left)
            if node.right:
                que.append(node.right)
        parents = len(que)
        level += 1
    return level


@dataclass
class NodeInfo:
    height: int = 0
    size: int = 0
    leaf_count: int = 0
    is_full: bool = True
    is_complete: bool = True


def collect(root):
    level = 0
    size = 0
    leaf_count = 0
    is_full = True
    is_complete = True

    seen_not_filled = False

    for node, lvl in iter.level_order(root):
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
