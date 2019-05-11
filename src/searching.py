import random

from src.algorithms.searching.binarysearch import binary_search


def setup_binary_search(array, key):
    return [array, 0, len(array) + 1, key]


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

    # Create set to remove duplicates and recreate list from set and sort it
    array = sorted(list(set(array)))

    # Set value to search for
    key = array[12]

    print("Searching for value", key, "at index", 12, "in list", array)

    # Setup algorithm
    if algorithm is binary_search:
        args = setup_binary_search(array, key)
    else:
        raise ValueError("Could not match algorithm to any function arguments")

    # Call function and unwrap list of args
    return_val = algorithm(*args)

    # Print results and linebreak
    if key == array[return_val]:
        print("Index for", key, "found at", return_val)
    else:
        print("Key not found!")
    print()


run_algorithm(binary_search)
