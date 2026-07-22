# Count Negative Multiples of 3

def neg_mul_of_3(lst):
    count = 0
    for num in lst:
        if num<0 and num%3==0:
            count+=1
    return count

# Time complexity: O(n)
# Space complexity: O(1)