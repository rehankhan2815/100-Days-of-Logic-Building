# Given a list of integers and a target, return how many numbers are greater than the target.

def greater_than(lst, target):
    count = 0
    for num in lst:
        if num > target:
            count += 1
    return count

#Time: O(n)
#Space: O(1)