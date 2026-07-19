# Find last even number 

def last_even(lst):
  last_even= None
  for num in lst:
    if num%2==0:
      last_even= num
  return last_even

# Time Complexity= O(n) worst case 
# Space complexity= O(1)