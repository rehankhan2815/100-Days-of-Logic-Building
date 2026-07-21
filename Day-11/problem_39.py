# Count Numbers Greater Than the Average

def greater_than_avg(lst):

    if len(lst) == 0:
        return 0

    total=0
    for num in lst:
        total+=num
    avg= total/len(lst)
    count = 0
    for num in lst:
        if num > avg:
            count+=1
    return count 

# Time complexity: O(n)
# Space complexity: O(1)