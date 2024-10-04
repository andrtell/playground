import math

from hypothesis import given, strategies as st

import dsa.util as util

from dsa.binary_tree.query import Query
from dsa.binary_tree import AVLTree, avltree


@given(st.integers(1, 100), st.integers(1, 10000))
def test_op_insert(count, seed):
    s = util.random_list(count, 0, 1000, seed=seed)
    t = AVLTree()
    for v in s:
        t.insert(v)
    assert len(t) == len(set(s))
    for v in s:
        assert v == t.find(v)


@given(st.integers(1, 100), st.integers(1, 10000))
def test_op_delete(size, seed):
    s = util.random_list(size, 0, 100, seed=seed)
    t = avltree(s)
    for v in s:
        t.delete(v)
        assert t.find(v) is None
    assert not t


@given(st.integers(0, 100), st.integers(1, 10000))
def test_in_order_is_sorted(size, seed):
    s = util.random_list(size, 0, 100, seed=seed)
    t = avltree(s)
    s = list(set(s))
    s.sort()
    assert list(t) == s


@given(st.integers(1, 100), st.integers(1, 10000))
def test_min_value(size, seed):
    s = util.random_list(size, 0, 1000, seed=seed)
    t = avltree(s)
    assert t.min() == min(s)


@given(st.integers(1, 100), st.integers(1, 10000))
def test_max_value(size, seed):
    s = util.random_list(size, 0, 1000, seed=seed)
    t = avltree(s)
    assert t.max() == max(s)


@given(st.integers(1, 30), st.integers(1, 10000))
def test_is_balanced_after_insert(size, seed):
    s = util.random_list(size, 0, 100, seed=seed)
    t = avltree(s[:-1])
    assert abs(Query.balance(t.root)) < 2
    t.insert(s[-1])
    assert abs(Query.balance(t.root)) < 2


@given(st.integers(1, 30), st.integers(1, 10000))
def test_is_balanced_after_delete(size, seed):
    s = util.random_list(size, 0, 100, seed=seed)
    t = avltree(s)
    assert abs(Query.balance(t.root)) < 2
    t.delete(s[0])
    assert abs(Query.balance(t.root)) < 2
