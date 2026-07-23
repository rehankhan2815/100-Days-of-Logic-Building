# Day 13

## Problem 51

* **Concept:** Count Positive Numbers Less Than Target
* **Time Complexity:** O(n)
* **Space Complexity:** O(1)
* **Lesson Learned:** Multiple conditions can be combined in a single `if` statement to filter elements efficiently.

## Problem 52

* **Concept:** Last Negative Number
* **Time Complexity:** O(n)
* **Space Complexity:** O(1)
* **Lesson Learned:** To find the last occurrence, traverse the entire list while updating the answer whenever a match is found.

## Problem 53

* **Concept:** Sum of Even Numbers Greater Than Target
* **Time Complexity:** O(n)
* **Space Complexity:** O(1)
* **Lesson Learned:** Summation problems follow the same traversal pattern as counting problems; only the accumulator changes.

## Problem 54

* **Concept:** Smallest Positive Multiple of 3
* **Time Complexity:** O(n)
* **Space Complexity:** O(1)
* **Lesson Learned:** Minimum tracking can be combined with filtering conditions in a single traversal.

## Problem 55

* **Concept:** Count Odd Numbers Greater Than Average
* **Time Complexity:** O(n)
* **Space Complexity:** O(1)
* **Lesson Learned:** Some problems require two traversals. First compute the average, then perform the required counting. Also learned to avoid variable naming mistakes (`count` vs `count_odd`).

## Problem 56

* **Concept:** First Negative Even Number
* **Time Complexity:** O(n)
* **Space Complexity:** O(1)
* **Lesson Learned:** First occurrence problems should return immediately once the required element is found.

## Problem 57

* **Concept:** Largest Positive Multiple of 5
* **Time Complexity:** O(n)
* **Space Complexity:** O(1)
* **Lesson Learned:** Maximum tracking works the same regardless of the filtering condition.

## Problem 58

* **Concept:** Last Odd Number Less Than Target
* **Time Complexity:** O(n)
* **Space Complexity:** O(1)
* **Lesson Learned:** A small assignment mistake (`last = None` instead of `last = num`) can completely change the algorithm's behavior.

## Problem 59

* **Concept:** Count Numbers Divisible by Both 4 and 6
* **Time Complexity:** O(n)
* **Space Complexity:** O(1)
* **Lesson Learned:** Instead of checking `num % 4 == 0 and num % 6 == 0`, use the LCM:

  * `num % 12 == 0`

## Problem 60

* **Concept:** Count Occurrences of the Maximum Element
* **Time Complexity:** O(n)
* **Space Complexity:** O(1)
* **Lesson Learned:** Initially solved using two traversals (find maximum, then count). Optimized it into a one-pass solution by maintaining both the maximum and its count simultaneously.

## Extra Insights

### 💡 One-Pass Optimization

* Instead of solving related tasks separately, try maintaining multiple variables during a single traversal.
* Example:

  * Track the current maximum.
  * Track how many times it appears.
* When a new maximum is found:

  * Update the maximum.
  * Reset the count to `1`.
* When the current maximum appears again:

  * Increment the count.

### 🧠 Common Debugging Lesson

* Most errors today were not logic errors but:

  * Variable name mismatches.
  * Incorrect assignments.
  * Forgetting to initialize variables.

### 🚀 Milestone

* Completed **60 out of 100** logic-building problems.
* Started thinking about **algorithm optimization**, not just correctness.
* Learned to reduce multiple traversals into a single traversal when possible.
