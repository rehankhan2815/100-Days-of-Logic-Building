#Find smallest positive number in list return None if no positive number there.

import math
def smallest_positive(lst):
    minimum= math.inf
    for num in lst :
      
      if num>0 and num<minimum:
          minimum=num

      
    return None if minimum==math.inf else minimum

#Time Complexity: O(n)
#Space Complexity: O(1)