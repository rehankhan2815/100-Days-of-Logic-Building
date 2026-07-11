#Find largest even number in a list 

def largest_even(lst):
    largest = None

    for num in lst:
        if num % 2 == 0:
            if largest is None or num > largest:
                largest = num

    return largest

# Time Complexity: O(n)
# Space Complexity: O(1)