# Find the index of the first negative number in the list return -1 if no negative number 

def first_negative_index(lst):
  for i in range(len(lst)):
    if lst[i]<0:
      return i
  return -1

lst=[-7, 5, 8]
first_negative_index(lst)

#Time Complexity: O(n)
#Space Complexity: O(1)