def partition(array, p, r):
    """
    Partition the array[p..r] into two (possibly empty) sub-arrays array[p..q-1] and array[q+1..r], such that each
    element in the lower bound is less or equal to the pivot, and each element in the upper bound is greater than the
    pivot. Returns the index of the pivot upon completion.

    :param array: the array to sort
    :param p: the lower bound
    :param r: the upper bound
    :return: the index at which the pivot is placed
    """
    # Choose pivot at end
    x = array[r]
    # Setup lower partition counter
    i = p - 1
    # For each element in array[p..r-1]
    for j in range(p, r):
        # If current item is leq than pivot
        if array[j] <= x:
            # Increment i anticipating a swap
            i += 1
            # Swap values at indices i and j in array
            array[i], array[j] = array[j], array[i]
    # Swap pivot with first element of upper sub-array, such that array[p..i] <= pivot <= array[i+2..r]
    array[i + 1], array[r] = array[r], array[i + 1]
    # Return index of pivot for further sorting
    return i + 1


def quick_sort(array, p, r):
    """
    Quick-sorts given array with lower and upper bound supplied

    :param array: the array to sort
    :param p: lower bound
    :param r: upper bound
    :return: sorted array from lower to upper bound
    """
    if p < r:
        # Partition array[p..r]
        q = partition(array, p, r)
        # Recursively call quick-sort on lower partition
        quick_sort(array, p, q - 1)
        # Recursively call quick-sort on upper partition
        quick_sort(array, q + 1, r)
    return array
