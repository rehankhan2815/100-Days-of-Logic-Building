# Find number closest to zero return postive if absolute of number are equal

def closest_to_zero(lst):
    closest = None
    for num in lst:
        if closest is None or abs(num) < abs(closest):
            closest = num
        elif abs(num) == abs(closest):
            if num > closest:
                closest = num
    return closest

# Time complexity: O(n)
# Space complexity: O(1)