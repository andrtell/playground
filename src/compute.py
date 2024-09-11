import random

from collections.abc import Sequence


def random_list(
    count: int = 10, min: int = 0, max: int = 10, seed=None
) -> list[int]:
    random.seed(seed)
    return [random.randint(min, max) for _ in range(count)]


def is_sorted(items: Sequence[int]) -> bool:
    for i in range(len(items) - 1):
        if items[i] > items[i + 1]:
            return False

    return True


def shuffled(items: Sequence[int], seed=None) -> list[int]:
    random.seed(seed)
    return random.sample(items, len(items))


def is_permutation(a: Sequence[int], b: Sequence[int]) -> bool:
    return set(a) == set(b)


def insertion_sort(items: list[int]) -> None:
    for j in range(1, len(items)):
        key = items[j]
        i = j - 1
        while i >= 0 and key < items[i]:
            items[i + 1] = items[i]
            i -= 1

        items[i + 1] = key

    return None


def bubble_sort(items: list[int]) -> None:
    for j in range(len(items) - 1, 0, -1):
        for i in range(j):
            if items[i] > items[i + 1]:
                items[i], items[i + 1] = items[i + 1], items[i]

    return None


def selection_sort(items: list[int]) -> None:
    for j in range(0, len(items)):
        min = j
        for i in range(j + 1, len(items)):
            if items[i] < items[min]:
                min = i
        items[j], items[min] = items[min], items[j]

    return None


def merge_sort(items: list[int]) -> None:
    merge_sort_low_high(items, 0, len(items), items[:])

    return None


def merge_sort_low_high(items: list[int], low, high, copy: list[int]):
    if high - low < 2:
        return None

    mid = low + (high - low) // 2

    merge_sort_low_high(copy, low, mid, items)
    merge_sort_low_high(copy, mid, high, items)

    merge_sort_merge(items, low, mid, high, copy)

    return None


def merge_sort_merge(items: list[int], low, mid, high, copy: list[int]):
    i = low
    j = mid

    for k in range(low, high):
        if i < mid and (j >= high or copy[i] <= copy[j]):
            items[k] = copy[i]
            i += 1
        else:
            items[k] = copy[j]
            j += 1

    return None


def heap_sort(items: list[int]):
    n = len(items)

    for i in range(n // 2, -1, -1):
        heap_sort_bubble_down(items, n, i)

    for j in range(n - 1, 0, -1):
        items[j], items[0] = items[0], items[j]
        heap_sort_bubble_down(items, j, 0)

    return None


def heap_sort_bubble_down(items: list[int], n: int, root: int):
    while True:
        max = root

        left = 2 * root

        if left < n and items[left] > items[max]:
            max = left

        right = left + 1

        if right < n and items[right] > items[max]:
            max = right

        if max == root:
            break

        items[root], items[max] = items[max], items[root]

        root = max

    return None
