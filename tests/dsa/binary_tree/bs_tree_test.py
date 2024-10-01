from hypothesis import given, strategies as st
import dsa.util as util
from dsa.binary_tree import BSTree


@given(st.integers(0, 100))
def test_sorted(count):
    src = util.random_list(count, 0, 100)
    t = BSTree()
    t.insert_from(src)
    src = list(set(src))
    src.sort()
    assert list(t) == src


@given(st.integers(1, 100))
def test_min(count):
    src = util.random_list(count, 0, 10000)
    t = BSTree()
    t.insert_from(src)
    assert t.min() == min(src)


@given(st.integers(1, 100))
def test_max(count):
    src = util.random_list(count, 0, 10000)
    t = BSTree()
    t.insert_from(src)
    assert t.max() == max(src)
