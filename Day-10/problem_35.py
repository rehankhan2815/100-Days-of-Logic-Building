# First Multiple of Both 3 and 5

def mul_of_3_5(lst):
    for num in lst :
        if num %15==0:
            return num
    return None

# Time Complexity: O(n) : worst case
# Space Complexity: O(1)