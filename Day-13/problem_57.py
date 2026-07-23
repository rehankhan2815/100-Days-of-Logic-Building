# Largest Positive Multiple of 5

def largest_pos(lst):
    largest= None
    for num in lst:
        if num%5==0 and num>0:
            if largest is None or num>largest:
                largest= num
    return largest

# Time complexity: O(n)
# Space complexity: O(1)