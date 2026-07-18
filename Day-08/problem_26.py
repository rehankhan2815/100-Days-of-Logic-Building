# Difference Between Largest and Second Largest

def diff(lst):
  second_largest= None
  largest= None
  for num in lst:
    if largest is None or num > largest:
      second_largest= largest
      largest= num
    elif (second_largest is None or num > second_largest) and num != largest:
      second_largest= num
  return largest-second_largest if second_largest is not None else None

#Time complexity= O(n)
# Space complexity= O(1)