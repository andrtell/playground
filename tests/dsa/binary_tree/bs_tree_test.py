from hypothesis import given, strategies as st
import dsa.util as util
from dsa.binary_tree import BSTree


@given(st.integers(0, 100), st.integers(1, 10000))
def test_sorted(count, seed):
    src = util.random_list(count, 0, 100, seed=seed)
    t = BSTree()
    t.insert_from(src)
    src = list(set(src))
    src.sort()
    assert list(t) == src


@given(st.integers(1, 100), st.integers(1, 10000))
def test_min(count, seed):
    src = util.random_list(count, 0, 1000, seed=seed)
    t = BSTree()
    t.insert_from(src)
    assert t.min() == min(src)


@given(st.integers(1, 100), st.integers(1, 10000))
def test_max(count, seed):
    src = util.random_list(count, 0, 1000, seed=seed)
    t = BSTree()
    t.insert_from(src)
    assert t.max() == max(src)


@given(st.integers(1, 100), st.integers(1, 10000))
def test_delete(count, seed):
    src = util.random_list(count, 0, 1000, seed=seed)
    t = BSTree()
    t.insert_from(src)
    for v in src:
        t.delete(v)
