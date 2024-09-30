from hypothesis import given, strategies as st

import ds.list.util as util


@given(st.integers(0, 23), st.integers(0, 100))
def test_random_list(count, seed):
    a = util.random_list(count, seed=seed)
    b = util.random_list(count, seed=seed)
    assert a == b


@given(st.integers(0, 23))
def test_is_sorted(count):
    src = util.random_list(count)
    dst = sorted(src)
    assert util.is_sorted(dst)


@given(st.integers(2, 23))
def test_is_not_sorted(count):
    src = util.random_list(count)
    while src == sorted(src):
        src = util.random_list(count)
    assert not util.is_sorted(src)


@given(st.integers(0, 23))
def test_is_permutation(count):
    a = util.random_list(count)
    b = util.shuffle_list(a)
    assert util.is_permutation(a, b)
