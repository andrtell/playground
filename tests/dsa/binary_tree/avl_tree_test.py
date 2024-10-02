import math
from hypothesis import given, strategies as st

import dsa.util as util
import dsa.binary_tree.info as info
from dsa.binary_tree import AVLTree, avltree


@given(st.integers(1, 100), st.integers(1, 10000))
def test_can_insert(count, seed):
    s = util.random_list(count, 0, 1000, seed=seed)
    t = AVLTree()
    for v in s:
        t.insert(v)


@given(st.integers(1, 100), st.integers(1, 10000))
def test_can_delete(size, seed):
    s = util.random_list(size, 0, 100, seed=seed)
    t = avltree(s)
    for v in s:
        t.delete(v)


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
def test_is_balanced_tree(size, seed):
    s = util.random_list(size, 0, 100, seed=seed)
    t = AVLTree()
    for v in s:
        t.insert(v)
        assert abs(info.balance(t.root)) < 2
    for v in s:
        t.delete(v)
        assert abs(info.balance(t.root)) < 2


@given(st.integers(1, 30), st.integers(1, 10000))
def test_height_property(size, seed):
    s = util.random_list(size, 0, 100, seed=seed)
    t = AVLTree()
    phi = (1 + math.sqrt(5)) / 2
    b = math.log2(5) / (2 * math.log2(phi))
    for v in s:
        t.insert(v)
        h = info.height(t.root)
        assert math.log2(t.size + 1) <= h and h < math.log(t.size + 2, phi) + b
    for v in s:
        t.delete(v)
        h = info.height(t.root)
        assert math.log2(t.size + 1) <= h and h < math.log(t.size + 2, phi) + b
