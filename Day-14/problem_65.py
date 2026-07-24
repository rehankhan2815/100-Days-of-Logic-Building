#

def first_repeat(lst):
    seen = set()

    for num in lst:
        if num > 0:
            if num in seen:
                return num
            seen.add(num)

    return None

# DISCARDED DICT SOLUTION   because it requires '1' anfd stores key and value both but set store keys only
# Time: O(n)
# Space: O(n)