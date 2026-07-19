# Last Index of Target

def last_target(lst, target):
    index = -1
    for i in range(len(lst)):
        if lst[i] == target:
            index = i
    return index

# Time Complexity: O(n)
# Space Complexity: O(1)