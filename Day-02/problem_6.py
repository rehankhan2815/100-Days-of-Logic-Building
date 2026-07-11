# Find sum of positive number in a list 

def sum_positive(lst):
  total= 0
  for num in lst:
    if num>0 :
      total+=num
  return total

lst= [-1, -2, -3]
sum_positive(lst)

# Time Complexity: O(n)
# Space Complexity: O(1)