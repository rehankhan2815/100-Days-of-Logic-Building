#  Find the Difference Between Largest and Smallest

import math

def diff(lst):
    if len(lst) == 0:
        return None

    largest = -math.inf
    smallest = math.inf

    for num in lst:
        if num < smallest:
            smallest = num
        if num > largest:
            largest = num

    return largest - smallest