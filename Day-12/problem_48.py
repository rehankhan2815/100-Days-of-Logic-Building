# Last index of even number 

def last_index_even(lst):
  index= -1
  for i in range(0, len(lst)):
    if lst[i] % 2 ==0:
      index= i
  return index

# Time complexity: O(n)
# Space complexity: O(1)