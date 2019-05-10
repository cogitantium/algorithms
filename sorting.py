import random

from algorithms import insertionsort, bubblesort


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

    print("Unsorted:\t", unsorted_list)
    print("Correct:\t", sorted(unsorted_list))

    # Call function
    sorted_list = algorithm(unsorted_list)

    print("Sorted:\t\t", sorted_list)

    # Print results and linebreak
    if sorted(unsorted_list) == sorted_list:
        print("List is sorted")
    else:
        print("Not sorted!")
    print()


run_algorithm(bubblesort.bubble_sort)
run_algorithm(insertionsort.insertion_sort)
