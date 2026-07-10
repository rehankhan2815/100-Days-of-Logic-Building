# Finding Largest Element

def maxim(lst): 
    largest = lst[0]

    for i in range(1, len(lst)):
        if lst[i] > largest:
            largest = lst[i]

    return largest

# Time Complexity: O(n)
# Space Complexity: O(1)