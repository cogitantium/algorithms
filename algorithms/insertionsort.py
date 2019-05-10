def insertion_sort(input_list):
    """
    Insertion-sorts input by iterating over index 1 to input-length and for each setting a key which is to be
    inserted, this key is then inserted towards the beginning of the list, if the list is not yet exhausted and the
    next item is greater than the key.

    :param input_list: the input to sort
    :return: the input sorted in-place
    """
    for j in range(1, len(input_list)):
        key = input_list[j]
        i = j - 1
        while i >= 0 and input_list[i] > key:
            input_list[i + 1] = input_list[i]
            i -= 1
        input_list[i + 1] = key
    return input_list
