from hypothesis import given, strategies as st
import dsa.util as util
from dsa.binary_tree import BSTree, bstree


@given(st.integers(1, 100), st.integers(1, 10000))
def test_op_insert(size, seed):
    s = util.random_list(size, 0, 1000, seed=seed)
    t = BSTree()
    for v in s:
        t.insert(v)
    assert len(t) == len(set(s))
    for v in s:
        assert v == t.find(v)


@given(st.integers(1, 100), st.integers(1, 10000))
def test_op_delete(size, seed):
    s = util.random_list(size, 0, 100, seed=seed)
    t = bstree(s)
    for v in s:
        t.delete(v)
        assert t.find(v) is None
    assert not t


@given(st.integers(0, 100), st.integers(1, 10000))
def test_in_order_is_sorted(size, seed):
    s = util.random_list(size, 0, 100, seed=seed)
    t = bstree(s)
    s = list(set(s))
    s.sort()
    assert list(t) == s


@given(st.integers(1, 100), st.integers(1, 10000))
def test_min_value(count, seed):
    s = util.random_list(count, 0, 1000, seed=seed)
    t = bstree(s)
    assert t.min() == min(s)


@given(st.integers(1, 100), st.integers(1, 10000))
def test_max_value(count, seed):
    s = util.random_list(count, 0, 1000, seed=seed)
    t = bstree(s)
    assert t.max() == max(s)
