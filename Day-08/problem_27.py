#Find second largest even number 

def second_largest_even(lst):
  largest= None
  second_largest= None
  for num in lst :
    if num%2==0:
      if largest is None or num > largest:
        second_largest= largest
        largest= num
      elif (second_largest is None or num > second_largest) and num != largest:
        second_largest= num
  return second_largest

#Time complexity= O(n)
# Space complexity= O(1)
