# Smallest Multiple of 5

def smallest_mul_5(lst):
  smallest= None 
  for num in lst:
    if num%5==0:
      if smallest is None or num<smallest:
        smallest= num

  return smallest

# Time complexity: O(n)
# Space complexity: O(1)