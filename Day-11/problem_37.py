# Sum of Negative Odd Numbers

def sum_neg_od(lst):
    total= 0
    for num in lst:
        if num<0 and num%2!=0:
            total+=num
    return total

# Time complexity: O(n)
# Space complexity: O(1)