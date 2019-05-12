import random

from src.algorithms.sorting import bubblesort, insertionsort
from src.algorithms.sorting.mergesort import merge_sort
from src.algorithms.sorting.quicksort import quick_sort
from src.algorithms.sorting.selectionsort import selection_sort


def setup_merge_sort(array):
    return [array, 0, len(array) - 1]


def setup_quick_sort(array):
    return [array, 0, len(array) - 1]


def run_algorithm(algorithm):
    """
    Runs algorithm and prints debug information on success and input and output

    :param algorithm: the algorithm to sort input with
    :return:
    """
    print("Sorting with", algorithm.__name__)

    # Initialise unsorted list
    unsorted_list = []

    # Populate with random integers
    for i in range(10):
        unsorted_list.append(random.randint(0, 99))

    # Create new correct list
    correct_list = sorted(unsorted_list)

    print("Unsorted:\t\t\t", unsorted_list)

    # Call function and setup call if necessary
    if algorithm is merge_sort:
        sorted_list = algorithm(*setup_merge_sort(unsorted_list))
    elif algorithm is quick_sort:
        sorted_list = algorithm(*setup_quick_sort(unsorted_list))
    else:
        sorted_list = algorithm(unsorted_list)

    print("Correct:\t\t\t", correct_list)
    print("Algorithm-sorted:\t", sorted_list)

    # Print results and linebreak
    if correct_list == sorted_list:
        print("List is sorted")
    else:
        print("Not sorted!")
    print()


run_algorithm(bubblesort.bubble_sort)
run_algorithm(insertionsort.insertion_sort)
run_algorithm(merge_sort)
run_algorithm(selection_sort)
run_algorithm(quick_sort)
