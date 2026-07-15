# return largest positive number 

def largest_positive(lst):
    largest = None
    for num in lst:
        if num > 0:
            if largest is None:
                largest = num
            elif num > largest:
                largest = num
    return largest

#Time complexity: O(n)
#Space complexity: O(1)