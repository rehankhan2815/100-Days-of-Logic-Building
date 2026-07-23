# First Negative Even Number

def first_neg_even(lst):
    for num in lst:
        if num <0 and num%2==0:
            return num
    return None

# Time complexity: O(n)
# Space complexity: O(1)