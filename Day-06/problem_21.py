# Find smallest odd number 

def smallest_odd(lst):
  smallest= None 
  for num in lst:
    if num%2!=0 :
      if smallest is None :
        smallest = num
      elif num < smallest:
        smallest= num
  return smallest

#Time complexity: O(n)
#Space complexity: O(1)