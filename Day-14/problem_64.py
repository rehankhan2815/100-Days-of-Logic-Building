# Find max frequesncy number and return greater number if two have same value

def freq_neg(lst):
    seen = {}

    for num in lst:
        if num < 0:
            if num not in seen:
                seen[num] = 1
            else:
                seen[num] += 1

    if len(seen) == 0:
        return None

    max_freq = None
    for v in seen.values():
        if max_freq is None or v > max_freq:
            max_freq = v

    candidate = []

    for k in seen:
        if seen[k] == max_freq:
            candidate.append(k)

    return max(candidate)
'''
Time Complexity:
    Counting frequencies → O(n)
    Finding max frequency → O(m)
    Collecting candidates → O(m)
    max(candidate) → O(k)
n = length of list
m = number of distinct negative numbers

Space:
    O(m)'''

# Optimized one tooo:
def freq_neg(lst):
    seen = {}

    for num in lst:
        if num < 0:
            if num not in seen:
                seen[num] = 1
            else:
                seen[num] += 1

    if len(seen) == 0:
        return None

    best_num = None
    best_freq = 0

    for num in seen:
        if (
            seen[num] > best_freq
            or (
                seen[num] == best_freq
                and (best_num is None or num > best_num)
            )
        ):
            best_freq = seen[num]
            best_num = num

    return best_num

'''
Time Complexity:
    O(n + m)
Space Complexity:
    O(m)
'''