# First Number Divisible by 7

def mul_of_7(lst):
    for num in lst :
        if num%7==0:
            return num
    return None

# Time complexity: O(n)
# Space complexity: O(1)