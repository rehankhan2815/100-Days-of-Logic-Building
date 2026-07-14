# Find average of positive numbers in a list if any alse return None

def average(lst):
    count = 0
    total = 0

    for num in lst:
        if num > 0:
            count += 1
            total += num

    if count == 0:
        return None

    return total / count

# Time Complexity: O(n)
# Space Complexity: O(1)