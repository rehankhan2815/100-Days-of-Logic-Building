# difference between smallest and largest even number 

def diff(lst):
    smallest = None
    largest = None

    for num in lst:
        if num % 2 == 0:
            if smallest is None or num < smallest:
                smallest = num
            if largest is None or num > largest:
                largest = num

    if smallest is None:
        return None

    return largest - smallest

# Time complexity: O(n)
# Space complexity: O(1)