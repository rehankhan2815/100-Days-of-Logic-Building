# Sum of Positive Odd Numbers Less Than Target

def sum_odd(lst, target):
    total= 0
    for num in lst:
        if num>0 and num%2!=0 and num<target:
            total+=num
    return total

# Time complexity: O(n)
# Space complexity: O(1)