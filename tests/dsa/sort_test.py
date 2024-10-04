from hypothesis import given, strategies as st

import dsa.sort as sort
import dsa.util as util


@given(st.integers(0, 23), st.integers(-100, 0), st.integers(0, 100))
def test_insertion_sort(size, min, max):
    src = util.random_list(size, min, max)
    dst = src[:]
    sort.insertion_sort(dst)
    assert util.is_permutation(src, dst)
    assert util.is_sorted(dst)


@given(st.integers(0, 23))
def test_bubble_sort(size):
    src = util.random_list(size)
    dst = src[:]
    sort.bubble_sort(dst)
    assert util.is_permutation(src, dst)
    assert util.is_sorted(dst)


@given(st.integers(0, 23))
def test_selection_sort(size):
    src = util.random_list(size)
    dst = src[:]
    sort.selection_sort(dst)
    assert util.is_permutation(src, dst)
    assert util.is_sorted(dst)


@given(st.integers(0, 23))
def test_merge_sort(size):
    src = util.random_list(size)
    dst = src[:]
    sort.merge_sort(dst)
    assert util.is_permutation(src, dst)
    assert util.is_sorted(dst)


@given(st.integers(0, 23))
def test_heap_sort(size):
    src = util.random_list(size)
    dst = src[:]
    sort.heap_sort(dst)
    assert util.is_permutation(src, dst)
    assert util.is_sorted(dst)


@given(st.integers(0, 23))
def test_quick_sort(size):
    src = util.random_list(size)
    dst = src[:]
    sort.quick_sort(dst)
    assert util.is_permutation(src, dst)
    assert util.is_sorted(dst)


@given(st.integers(0, 23), st.integers(0, 100))
def test_sizeing_sort(size, k):
    src = util.random_list(size, max=k)
    dst = sort.counting_sort(src, k)
    assert util.is_permutation(src, dst)
    assert util.is_sorted(dst)
