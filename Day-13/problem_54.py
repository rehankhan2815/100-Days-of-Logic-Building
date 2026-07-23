#  Smallest Positive Multiple of 3

def smallest_pos(lst):
    smallest= None
    for num in lst:
        if num %3 ==0 and num>0:
            if smallest is None or num < smallest:
                smallest =num
    return smallest

# Time complexity: O(n)
# Space complexity: O(1)