import random

from src.algorithms.searching.binarysearch import binary_search


def run_algorithm(algorithm):
    """
    Runs algorithm and prints debug information on success and input and output

    :param algorithm: the algorithm to search input with
    :return: the index for a given value or None if not found
    """
    print("Searching with", algorithm.__name__)

    # Initialise unsorted list
    array = []

    # Populate with random integers
    for i in range(20):
        array.append(random.randint(0, 99))

    # Create set from list
    array_set = set(array)

    # Recreate list from set and sort it
    array = sorted(list(array_set))

    # Set value to search for
    key = array[12]

    # Call function
    return_val = algorithm(array, 0, len(array) + 1, key)

    # Print results and linebreak
    if key == array[return_val]:
        print("Index for", key, "found at", return_val)
    else:
        print("Key not found!")
    print()


run_algorithm(binary_search)
