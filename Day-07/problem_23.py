# Find largest negative number 

def largest_negative(lst):
  largest= None
  for num in lst:
    if num < 0:
      if largest is None or largest<num:
        largest= num
      
  return largest

#Time complexity: O(n)
#Space complexity: O(1)