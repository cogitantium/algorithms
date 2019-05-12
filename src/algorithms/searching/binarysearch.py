from math import floor


def binary_search(array, left, right, value):
    """
    Recursive binary search using divide-and-conquer.

    :param array: the input array to search, sorted and ascending
    :param left: lower bound
    :param right: upper bound
    :param value: the value being searched for
    :return: the index of value being searched for, if present, else return None
    """
    # Trivial case - if bounds are equal, check if found, and return index, or fail
    if left == right:
        if array[left] == value:
            return left
        else:
            return None
    middle = floor((left + right) / 2)  # Find middle

    # Divide and conquer, if value is in lower half, then dispatch search there, else in upper
    if array[middle] >= value:
        return binary_search(array, left, middle, value)
    else:
        return binary_search(array, middle + 1, right, value)
