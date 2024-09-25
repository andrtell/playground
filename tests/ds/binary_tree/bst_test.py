from ds.binary_tree.tree import Tree

from hypothesis import given, strategies as st

import ds.list.util as util


@given(st.integers(0, 100))
def test_sorted(count):
    src = util.random_list(count, 0, 100)
    tree = Tree()
    for v in src:
        tree.insert(v)
    src = list(set(src))
    src.sort()
    assert list(tree) == src
