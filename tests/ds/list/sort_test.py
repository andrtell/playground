from hypothesis import given, strategies as st

import ds.list.sort as sort
import ds.list.util as util


@given(st.integers(0, 23), st.integers(-100, 0), st.integers(0, 100))
def test_insertion_sort(count, min, max):
    src = util.random_list(count, min, max)
    dst = src[:]
    sort.insertion_sort(dst)
    assert util.is_permutation(src, dst)
    assert util.is_sorted(dst)


@given(st.integers(0, 23))
def test_bubble_sort(count):
    src = util.random_list(count)
    dst = src[:]
    sort.bubble_sort(dst)
    assert util.is_permutation(src, dst)
    assert util.is_sorted(dst)


@given(st.integers(0, 23))
def test_selection_sort(count):
    src = util.random_list(count)
    dst = src[:]
    sort.selection_sort(dst)
    assert util.is_permutation(src, dst)
    assert util.is_sorted(dst)


@given(st.integers(0, 23))
def test_merge_sort(count):
    src = util.random_list(count)
    dst = src[:]
    sort.merge_sort(dst)
    assert util.is_permutation(src, dst)
    assert util.is_sorted(dst)


@given(st.integers(0, 23))
def test_heap_sort(count):
    src = util.random_list(count)
    dst = src[:]
    sort.heap_sort(dst)
    assert util.is_permutation(src, dst)
    assert util.is_sorted(dst)


@given(st.integers(0, 23))
def test_quick_sort(count):
    src = util.random_list(count)
    dst = src[:]
    sort.quick_sort(dst)
    assert util.is_permutation(src, dst)
    assert util.is_sorted(dst)


@given(st.integers(0, 23), st.integers(0, 100))
def test_counting_sort(count, k):
    src = util.random_list(count, max=k)
    dst = sort.counting_sort(src, k)
    assert util.is_permutation(src, dst)
    assert util.is_sorted(dst)
