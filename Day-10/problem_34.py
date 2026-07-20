# Given a list of integers, return the index of the first negative number.
# If there is no negative number, return -1.

def first_negative(lst):
  for i in range(len(lst)):
    if lst[i]<0:
      return i
  return -1

# Time Complexity: O(n)
# Space Complexity: O(1)