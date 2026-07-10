# Find Second Largest Element

def sec_largest(lst):
  second_largest=float('-inf')
  largest=lst[0]
  if len(lst)==1:
    return lst[0]
  else:
    for i in range(1, len(lst)):
      if lst[i]>largest:
        second_largest=largest
        largest=lst[i]
      elif lst[ i]>second_largest:
        second_largest=lst[i]
    return second_largest
  
# Time Complexity: O(n)
# Space Complexity: O(1)
# Lesson Learned: Initialization matters, 
