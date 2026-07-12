# Find first positive number in a given list 

def first_positive(lst):
  if len(lst)==0:
    return None
  for num in lst:
    if num>0:
      return num
  return None 
 
 #Time Complexity: O(n) (worst case)
#Space Complexity: O(1)