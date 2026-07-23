# Count Number divisible by 4 and 6 

def divisible_by_4_6(lst):
    count= 0
    for num in lst :
        if num%12==0 :
            count+=1
    return count 

# Time complexity: O(n)
# Space complexity: O(1)