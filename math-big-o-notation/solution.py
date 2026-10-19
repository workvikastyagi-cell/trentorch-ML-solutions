def count_comparisons_linear_search(arr, target):
    """
    arr:    a list of numbers
    target: the value being searched for

    Returns:
        (found, comparisons): found is True if target is in arr, False
        otherwise. comparisons is the number of element-to-target
        comparisons actually performed (stop as soon as a match is
        found -- don't keep scanning).
    """
    # TODO: Implement a left-to-right linear scan, counting comparisons.
    found= False
    count= 0
    for i in arr:
        count += 1
        if i == target:
            return True, count
    return False, count


def count_comparisons_binary_search(sorted_arr, target):
    """
    sorted_arr: a list of numbers, already sorted ascending
    target:     the value being searched for

    Returns:
        (found, comparisons): same shape as count_comparisons_linear_search,
        but using binary search -- each comparison must actually halve
        the remaining search space.
    """
# TODO: Implement binary search from Theory, counting one
# comparison per midpoint check.
    lo, hi = 0, len(sorted_arr) - 1
    count = 0
    while lo <= hi:
        mid = (lo + hi) // 2
        count += 1
        if sorted_arr[mid] == target:
            return True, count
        elif sorted_arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return False, count
