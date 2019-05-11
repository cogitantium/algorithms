def iterative_factorial(n):
    """
    Iteratively computes the factorial of input

    :param n: the input
    :return: the factorial of input
    """
    # Initialise factorial to 1 - the base-case
    fac = 1
    # From 1 to n, multiply running factorial with next
    for i in range(1, n + 1):
        fac = fac * i
    return fac
