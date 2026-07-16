# count numbers divisible by 2 and 5

def divisibilty_bonus(lst):
    count = 0
    for num in lst:
        if num % 10 == 0:
            count += 1
    return count

#Time complexity: O(n)
#Space complexity: O(1)