import random as r
from collections import defaultdict


def random_list(count=10, min=0, max=10, seed=None):
    r.seed(seed)
    return [r.randint(min, max) for _ in range(count)]


def shuffle_list(lst, seed=None):
    r.seed(seed)
    return r.sample(lst, len(lst))


def is_sorted(ls):
    for i in range(len(ls) - 1):
        if ls[i] > ls[i + 1]:
            return False

    return True


def is_permutation(a, b):
    if len(a) != len(b):
        return False

    hmap = defaultdict(int)

    for v in a:
        hmap[v] += 1

    for v in b:
        if v not in hmap or hmap[v] == 0:
            return False

        hmap[v] -= 1

    return True
