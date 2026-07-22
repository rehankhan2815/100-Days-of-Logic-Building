# Count Numbers Between Two Values (Exclusive)

def in_between(lst, t1, t2):
    count = 0
    for num in lst:
        if num >t1 and num <t2:
            count+=1
    return count

# Time complexity: O(n)
# Space complexity: O(1)