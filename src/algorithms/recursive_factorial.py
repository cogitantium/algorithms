def recursive_factorial(n):
    """
    Recursively computes the factorial of input

    :param n: the input
    :return: the factorial of input
    """
    # If n is 1, then return 1 - the trivial case
    if n == 1:
        return 1
    # Otherwise multiply n by the result of factorial less one - the divide and conquer step
    else:
        return n * recursive_factorial(n - 1)
