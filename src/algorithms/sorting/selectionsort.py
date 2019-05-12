def selection_sort(array):
    """
    Selection sort iterates the array, and upon finding a lesser value in the sub-array array[i+1..n],
    swaps the value with array[i]. Time complexity is O(n^2) since operations are ~(n-1)*(n/2) as it iterates the
    array twice. Space complexity is O(n), as it sorts in-place.

    :param array: the array to be sorted
    :return: the sorted array
    """
    # Iterate array[0..n-1]
    for i in range(0, len(array)):
        # Set first element to minimum
        minimum = i
        # Search remaining array for a smaller value and save index in minimum
        for j in range(i + 1, len(array)):
            # If value at current index is less than previously found minimum, set new minimum index
            if array[j] < array[minimum]:
                minimum = j
        # Once minimum of sub-array array[i+1..n] is found, swap value between current and found minimum
        array[i], array[minimum] = array[minimum], array[i]
    return array
