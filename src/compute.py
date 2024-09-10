import random

from collections.abc import Sequence


def random_list(
    count: int = 10, min: int = 0, max: int = 10, seed=None
) -> list[int]:
    random.seed(seed)
    return [random.randint(min, max) for _ in range(count)]


def is_sorted(items: Sequence[int]) -> bool:
    return items == sorted(items)


def shuffled(items: Sequence[int], seed=None) -> list[int]:
    random.seed(seed)
    return random.sample(items, len(items))


def is_permutation(a: Sequence[int], b: Sequence[int]) -> bool:
    return set(a) == set(b)


def insertion_sort(items: Sequence[int]) -> list[int]:
    for j in range(1, len(items)):
        key = items[j]
        i = j - 1
        while i >= 0 and key < items[i]:
            items[i + 1] = items[i]
            i -= 1

        items[i + 1] = key


def bubble_sort(items: Sequence[int]) -> list[int]:
    pass
