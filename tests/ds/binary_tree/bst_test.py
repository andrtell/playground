from ds.binary_tree.bst import BSTree
from hypothesis import given, strategies as st

import ds.list.util as util


@given(st.integers(0, 100))
def test_sorted(count):
    src = util.random_list(count, 0, 100)
    tree = BSTree()
    for v in src:
        tree.insert(v)
    src = list(set(src))
    src.sort()
    assert list(tree) == src
