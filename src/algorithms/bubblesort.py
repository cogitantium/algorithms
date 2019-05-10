def bubble_sort(input_list):
    """
    Bubble-sorts input by iterating input-length passes and for each iterating backwards from input-length -1 down-to
    1 and swapping if index - 1 is greater than index

    :param input_list: the input to sort
    :return: the input sorted in-place
    """
    # For i = 0 to length
    for i in range(0, len(input_list) + 1):
        # For j = length - 1 to i - 1
        for j in range(len(input_list) - 1, i - 1, -1):
            if input_list[j - 1] > input_list[j]:
                # Swap
                input_list[j], input_list[j - 1] = input_list[j - 1], input_list[j]

    return input_list

