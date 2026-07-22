# First positive multiple of 6

def first_pos_mul_of_6(lst):

  for num in lst :
    
    if num>0  and num%6==0:
      return num

  return None

# Time complexity: O(n)
# Space complexity: O(1)