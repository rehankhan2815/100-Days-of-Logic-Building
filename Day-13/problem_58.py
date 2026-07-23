# Last Odd Number Less Than Target

def last_odd(lst, target):
    last= None
    for num in lst :
        if num % 2!=0 and num<target :
            last= num
    return last

# Time complexity: O(n)
# Space complexity: O(1)