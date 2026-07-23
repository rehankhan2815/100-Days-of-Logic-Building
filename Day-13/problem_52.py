# Last Negative Number

def last_negative(lst):
    last = None
    for num in lst:
        if num < 0:
            last = num
    return last

# Time complexity: O(n)
# Space complexity: O(1)