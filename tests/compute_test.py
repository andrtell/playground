import compute

from hypothesis import example, given, strategies as st


@given(st.integers(0, 23), st.integers(0, 100))
def test_random_list(count, seed):
    a = compute.random_list(count, seed=seed)
    b = compute.random_list(count, seed=seed)
    assert a == b


@given(st.integers(0, 23))
def test_is_sorted(count):
    src = compute.random_list(count)
    ord = sorted(src)
    assert compute.is_sorted(ord)


@given(st.integers(2, 23))
def test_is_not_sorted(count):
    src = compute.random_list(count)
    while src == sorted(src):
        src = compute.random_list(count)
    assert not compute.is_sorted(src)


@given(st.integers(0, 23))
def test_is_permutation(count):
    a = compute.random_list(count)
    b = compute.shuffled(a)
    assert compute.is_permutation(a, b)


@given(st.integers(0, 23), st.integers(-100, 0), st.integers(0, 100))
def test_insertion_sort(count, min, max):
    src = compute.random_list(count, min, max)
    ord = src[:]
    compute.insertion_sort(ord)
    assert compute.is_permutation(src, ord)
    assert compute.is_sorted(ord)


@given(st.integers(0, 23))
def test_bubble_sort(count):
    src = compute.random_list(count)
    ord = src[:]
    compute.bubble_sort(ord)
    assert compute.is_permutation(src, ord)
    assert compute.is_sorted(ord)


@given(st.integers(0, 23))
def test_selection_sort(count):
    src = compute.random_list(count)
    ord = src[:]
    compute.selection_sort(ord)
    assert compute.is_permutation(src, ord)
    assert compute.is_sorted(ord)
