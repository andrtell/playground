from hypothesis import given, strategies as st
from ds.binary_tree.bst import BSTree
import ds.list.util as util


@given(st.integers(0, 100))
def test_sorted(count):
    src = util.random_list(count, 0, 100)
    tree = BSTree()
    for v in src:
        tree.insert(v)
    src.sort()
    assert list(tree) == src
