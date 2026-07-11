# Counting even and odd both in one go 

def even_odd(lst):
  even = odd = 0
  for num in lst :
    if num%2==0:
      even+=1
    if num%2!=0:
      odd+=1
  return {"even": even, "odd":odd} 
lst= [1, 2, 3, 4, 5]
even_odd(lst)

# Time Complexity: O(n)
# Space Complexity: O(1)