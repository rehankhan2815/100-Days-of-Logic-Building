# Count Occurrences of a Target

def count_target(lst, target):
    count = 0
    for num in lst:
        if num == target:
            count += 1
    return count

#Time Complexity: O(n)
#Space Complexity: O(1)