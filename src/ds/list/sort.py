# --- Bubble sort ---------------------


def bubble_sort(ls):
    for hi in range(len(ls) - 1, 0, -1):
        for lo in range(hi):
            if ls[lo] > ls[lo + 1]:
                ls[lo], ls[lo + 1] = ls[lo + 1], ls[lo]


# --- Selection sort -------------------


def selection_sort(ls):
    for lo in range(0, len(ls)):
        min = lo
        for hi in range(lo + 1, len(ls)):
            if ls[hi] < ls[min]:
                min = hi
        ls[lo], ls[min] = ls[min], ls[lo]


# --- Insertion sort -------------------


def insertion_sort(ls):
    for hi in range(1, len(ls)):
        it = ls[hi]
        lo = hi - 1

        while lo >= 0 and it < ls[lo]:
            ls[lo + 1] = ls[lo]
            lo -= 1

        ls[lo + 1] = it


# --- Counting sort --------------------


def counting_sort(ls, max):
    slots = [0] * (max + 1)

    for it in ls:
        slots[it] += 1

    for si in range(1, max + 1):
        slots[si] = slots[si - 1] + slots[si]

    sorted = ls[:]

    for it in ls:
        sorted[slots[it] - 1] = it
        slots[it] -= 1

    return sorted


# --- Heap sort ------------------------


def heap_sort(ls):
    sz = len(ls)

    for lo in range(sz // 2, -1, -1):
        bubble_down(ls, lo, sz)

    for end in range(sz - 1, 0, -1):
        ls[end], ls[0] = ls[0], ls[end]
        bubble_down(ls, 0, end)


def bubble_down(ls, lo, end):
    hi = lo
    while True:
        left = 2 * lo
        if left < end and ls[left] > ls[hi]:
            hi = left

        right = left + 1
        if right < end and ls[right] > ls[hi]:
            hi = right

        if hi == lo:
            break

        ls[lo], ls[hi] = ls[hi], ls[lo]

        lo = hi


# --- Merge sort -----------------------


def merge_sort(ls):
    merge_sort_sublist(ls, 0, len(ls), ls[:])


def merge_sort_sublist(ls, lo, hi, tmp):
    if hi - lo < 2:
        return
    mid = lo + (hi - lo) // 2

    merge_sort_sublist(tmp, lo, mid, ls)
    merge_sort_sublist(tmp, mid, hi, ls)

    merge_sublists(ls, lo, mid, hi, tmp)


def merge_sublists(ls, lo, mid, hi, lst_copy):
    i = lo
    j = mid
    for k in range(lo, hi):
        if i < mid and (j >= hi or lst_copy[i] <= lst_copy[j]):
            ls[k] = lst_copy[i]
            i += 1
        else:
            ls[k] = lst_copy[j]
            j += 1


# --- Quick sort ----------------------


def quick_sort(ls):
    quick_sort_sublist(ls, 0, len(ls))


def quick_sort_sublist(ls, lo, end):
    if end - lo < 2:
        return

    mid = partition_list(ls, lo, end)

    quick_sort_sublist(ls, lo, mid)
    quick_sort_sublist(ls, mid + 1, end)


def partition_list(ls, lo, end):
    pivot = ls[end - 1]

    for hi in range(lo, end - 1):
        if ls[hi] <= pivot:
            ls[lo], ls[hi] = ls[hi], ls[lo]
            lo += 1

    ls[lo], ls[end - 1] = ls[end - 1], ls[lo]

    return lo
