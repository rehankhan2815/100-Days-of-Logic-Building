# Counting positive numbers in a list 

def count_positive(lst):
  count= 0
  for i in range(0, len(lst)):
    if lst[i]>0:
      count+=1
  return count 

# Time Complexity: O(n)
# Space Complexity: O(1)