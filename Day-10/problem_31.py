# Find first even number in a list if exist else return None  

def first_even(lst):
  first_even=None
  for num in lst:
    if num%2==0:
      first_even= num
     
      return first_even

#Time Complexity: O(n) (worst case: even number is at the end or absent).
#Space Complexity: O(1)