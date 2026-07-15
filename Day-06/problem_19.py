# Count Positive Even Numbers

def positive_even(lst):
    count= 0
    for num in lst:
        if num>0 and num%2==0:
            count+=1
    return count

#Time complexity: O(n)
#Space complexity: O(1)