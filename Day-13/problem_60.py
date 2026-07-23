#  Count Numbers Equal to the Maximum
def count_number_of_max(lst):
    if len(lst) == 0:
        return 0

    max = None
    count = 0

    for num in lst:
        if max is None or num > max:
            max = num
            count = 1
        elif num == max:
            count += 1

    return count

# Time complexity: O(n)
# Space complexity: O(1)    