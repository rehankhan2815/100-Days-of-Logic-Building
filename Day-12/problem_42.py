# Count Numbers Outside the Range

def outside(lst, low, high):
    count = 0
    for num in lst :
        if num<low or num >high:
            count+=1
    return count

# Time complexity: O(n)
# Space complexity: O(1)