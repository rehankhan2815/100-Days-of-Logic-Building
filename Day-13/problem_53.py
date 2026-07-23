# Sum of Even Numbers Greater Than Target

def sum_of_even(lst, target):
    total= 0
    for num in lst:
        if num%2==0 and num> target :
            total+=num
    return total

# Time complexity: O(n)
# Space complexity: O(1)