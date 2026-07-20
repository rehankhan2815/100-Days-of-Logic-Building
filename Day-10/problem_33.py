# First Index Greater Than Target

def first_index(lst, target):
  for i in range(len(lst)):
    if lst[i]>target:
      return i
  return -1

# Time Complexity: O(n)
# Space Complexity: O(1)