# Count multiples of 3

def div_by_3(lst):
  count= 0
  for num in lst :
    if num%3==0:
      count+=1
  return count

#Time complexity: O(n)
#Space complexity: O(1)