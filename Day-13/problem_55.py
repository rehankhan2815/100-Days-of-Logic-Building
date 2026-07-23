# Count Odd Numbers Greater Than the Average

def odd_greater_than_avg(lst):
    total = 0
    count_odd = 0

    if len(lst) == 0:
        return 0

    for num in lst:
        total += num

    avg = total / len(lst)

    for num in lst:
        if num % 2 != 0 and num > avg:
            count_odd += 1

    return count_odd

# Time complexity: O(n)
# Space complexity: O(1)