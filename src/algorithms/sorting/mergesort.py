def merge(array, p, q, r):
    """
    This auxiliary function merges two sorted sequences in a 'combine' step of the merge-sort algorithm. Assuming
    that the sub-arrays array[p..q] and array[q+1..r] are in sorted order, the function merges them to form a single
    sorted sub-array that replaces the current sub-array[p..r]

    :param array: base-array reference for modifying in-place
    :param p: lower bound
    :param q: pivot
    :param r: upper bound
    :return: merged, sorted array from lower to upper bound (inclusive)
    """
    # Setting sentinel to 100 as integers to sort are in the range 0..99
    sentinel = 100

    # Compute size of lower and upper sub-arrays
    lower_size = q - p + 1
    upper_size = r - q

    # Define new sub-arrays to merge with extra slot for sentinel
    left = [sentinel] * (lower_size + 1)
    right = [sentinel] * (upper_size + 1)

    # Copy sub-arrays
    for i in range(0, lower_size):
        left[i] = array[p + i]

    for j in range(0, upper_size):
        right[j] = array[q + 1 + j]

    # Declare sub-array indices for merging
    i = 0
    j = 0

    # Copy sub-arrays into array from p to r (inclusive) - lowest value first
    for k in range(p, r + 1):
        if left[i] <= right[j]:
            array[k] = left[i]
            i += 1
        else:
            array[k] = right[j]
            j += 1

    # Assert that both sub-arrays have reached their respective sentinel
    assert i == len(left) - 1 and j == len(right) - 1


def merge_sort(array, p, r):
    """
    Merge-sorts given array with lower and upper bound supplied

    :param array: base-array reference for modifying in-place
    :param p: lower bound
    :param r: upper bound 
    :return: sorted array from lower to upper bound
    """

    if p < r:
        q = (p + r) // 2  # Find middle utilising integer-division for flooring
        merge_sort(array, p, q)
        merge_sort(array, q + 1, r)
        merge(array, p, q, r)
    return array
