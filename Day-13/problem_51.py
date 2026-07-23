# Count Positive Numbers Less Than Target

def pos_less(lst, target):
    count = 0
    for num in lst:
        if num > 0 and num<target:
            count+=1
    return count

# Time complexity: O(n)
# Space complexity: O(1)