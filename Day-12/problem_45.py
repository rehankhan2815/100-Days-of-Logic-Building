# Largest odd number 

def largest_odd(lst):
  largest= None
  for num in lst :
    if num%2!=0:
      if largest is None or num>largest:
        largest= num
  return largest

# Time complexity: O(n)
# Space complexity: O(1)