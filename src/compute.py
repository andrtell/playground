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
