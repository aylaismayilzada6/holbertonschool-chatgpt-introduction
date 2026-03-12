#!/usr/bin/python3
import sys

def factorial(n):
    """
    Description: Calculates the factorial of a non-negative integer using recursion.
                 The factorial of n (written as n!) is the product of all positive
                 integers less than or equal to n. By definition, 0! = 1.

    Parameters:
        n (int): A non-negative integer whose factorial is to be computed.

    Returns:
        int: The factorial of n. For example, factorial(4) returns 24
             because 4! = 4 × 3 × 2 × 1 = 24.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

f = factorial(int(sys.argv[1]))
print(f)
