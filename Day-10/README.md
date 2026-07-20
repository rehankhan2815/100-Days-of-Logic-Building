# Day 10

## Problem 31

* **Concept:** First Even Number
* **Time Complexity:** O(n)
* **Space Complexity:** O(1)
* **Lesson Learned:** First occurrence problems should return immediately when the required element is found, eliminating the need for an extra tracking variable.

## Problem 32

* **Concept:** First Odd Number Greater Than Target
* **Time Complexity:** O(n)
* **Space Complexity:** O(1)
* **Lesson Learned:** Multiple conditions can be combined using logical operators while still following the first occurrence pattern.

## Problem 33

* **Concept:** First Index Greater Than Target
* **Time Complexity:** O(n)
* **Space Complexity:** O(1)
* **Lesson Learned:** First occurrence logic applies equally to indices. Instead of returning the element, return its index.

## Problem 34

* **Concept:** First Negative Index
* **Time Complexity:** O(n)
* **Space Complexity:** O(1)
* **Lesson Learned:** Once the first matching element is found, return its index immediately to avoid unnecessary traversal.

## Problem 35

* **Concept:** First Multiple of Both 3 and 5
* **Time Complexity:** O(n)
* **Space Complexity:** O(1)
* **Lesson Learned:** Mathematical simplification can make conditions cleaner. Instead of checking `num % 3 == 0 and num % 5 == 0`, checking `num % 15 == 0` is shorter and equally correct.

## Bonus Learning

* **Concept:** Pattern Recognition
* **Lesson Learned:** Before writing code, identify the underlying pattern (first occurrence, last occurrence, tracking, counting, etc.). Once the pattern is recognized, only the condition changes while the overall algorithm remains the same.
