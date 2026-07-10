# Check if array is sorted or not 


def is_sorted(lst):
  if len(lst)==1 or len(lst)==0:
    return True
  else:
    for i in range(0, len(lst)-1):
      if lst[i]>lst[i+1]:
        return False
    return True
  
# Time Complexity: O(n)
# Space Complexity: O(1)
