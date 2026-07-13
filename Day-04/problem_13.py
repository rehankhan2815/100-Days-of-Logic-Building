#Check if all number is positive 

def is_positive(lst):
    for num in lst:
        if num < 0:
            return False
    return True

#Time: O(n) (worst case)
#Space: O(1)