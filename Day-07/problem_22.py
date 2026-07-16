# Find second snallest number 

def second_smallest(lst):
    smallest = None
    second_smallest = None

    for num in lst:
        if smallest is None or num < smallest:
            second_smallest = smallest
            smallest = num

        elif num != smallest and (second_smallest is None or num < second_smallest):
            second_smallest = num

    return second_smallest

#Time complexity: O(n)
#Space complexity: O(1)