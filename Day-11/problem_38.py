# Smallest Positive Even Number

def smallest_pos_even(lst):
  smallest =None 
  for num in lst:
    if num%2==0 and num>0:
      if smallest is None or smallest>num :
        smallest = num
  return smallest 

# Time complexity: O(n)
# Space complexity: O(1)