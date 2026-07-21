# Count positive even number 

def count_pos_even(lst):
  count= 0
  for num in lst :
    if num>0 and num%2==0:
      count+=1
  return count 

# Time complexity: O(n)
# Space complexity: O(1)