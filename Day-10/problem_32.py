# Find first odd number greater than target

def first_odd(lst, target):
  for num in lst :
    if num %2!=0 and num > target:
      return num
  return None

# Time Complexity: O(n)
# Space Complexity: O(1)