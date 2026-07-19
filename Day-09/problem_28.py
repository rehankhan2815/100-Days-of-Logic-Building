# Find last positive number 

def last_positive(lst):
  last_positive= None
  for num in lst:
    if num >0:
      last_positive= num
  return last_positive

# Time Complexity= O(n) worst case 
# Space complexity= O(1)