# Find sum of even numbers in a list 

def sum_of_even(lst):
    total = 0
    for num in lst:
        if num % 2 == 0:
            total += num
    return total

#Time: O(n)
#Space: O(1)