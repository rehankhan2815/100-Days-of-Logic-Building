# Largest Negative Even Number

def largest_neg_even(lst):
    largest= None
    for num in lst :
        if num<0 and num%2==0:
            if largest is None or largest <num:
                largest= num
    return largest

# Time complexity: O(n)
# Space complexity: O(1)