# Sum of Multiples of 4

def mul_of_4(lst):
  total= 0
  for num in lst:
    if num % 4==0:
      total+=num
  return total

# Time complexity: O(n)
# Space complexity: O(1)