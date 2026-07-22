# Day 12

## Problem 41

* **Concept:** Count Numbers Between Two Values (Exclusive)
* **Time Complexity:** O(n)
* **Space Complexity:** O(1)
* **Lesson Learned:** Counting problems can use multiple comparison conditions together, such as `low < num < high`.

## Problem 42

* **Concept:** Count Numbers Outside the Range
* **Time Complexity:** O(n)
* **Space Complexity:** O(1)
* **Lesson Learned:** Use the correct logical operator. Numbers outside a range satisfy `num < low OR num > high`, not `AND`.

## Problem 43

* **Concept:** Sum of Multiples of 4
* **Time Complexity:** O(n)
* **Space Complexity:** O(1)
* **Lesson Learned:** Summation problems follow the same traversal pattern as counting problems, with only the accumulator changing.

## Problem 44

* **Concept:** First Number Divisible by 7
* **Time Complexity:** O(n)
* **Space Complexity:** O(1)
* **Lesson Learned:** First occurrence problems should return immediately once the required element is found.

## Problem 45

* **Concept:** Largest Odd Number
* **Time Complexity:** O(n)
* **Space Complexity:** O(1)
* **Lesson Learned:** Maximum tracking can be combined with filtering conditions while using `None` as the initial value.

## Problem 46

* **Concept:** Smallest Multiple of 5
* **Time Complexity:** O(n)
* **Space Complexity:** O(1)
* **Lesson Learned:** Minimum tracking follows the same algorithm regardless of the filtering condition.

## Problem 47

* **Concept:** Count Negative Multiples of 3
* **Time Complexity:** O(n)
* **Space Complexity:** O(1)
* **Lesson Learned:** Multiple conditions can be combined into a single `if` statement for cleaner and more readable code.

## Problem 48

* **Concept:** Last Index of an Even Number
* **Time Complexity:** O(n)
* **Space Complexity:** O(1)
* **Lesson Learned:** Last occurrence problems require traversing the entire list while updating the stored index whenever a new match is found.

## Problem 49

* **Concept:** Difference Between Largest and Smallest Even Number
* **Time Complexity:** O(n)
* **Space Complexity:** O(1)
* **Lesson Learned:** Multiple tracking variables can be maintained simultaneously in a single traversal. A single even number automatically produces a difference of `0` because the largest and smallest values are the same.

## Problem 50

* **Concept:** First Positive Multiple of 6
* **Time Complexity:** O(n)
* **Space Complexity:** O(1)
* **Lesson Learned:** Empty-list checks are sometimes unnecessary. A function can naturally return the default value after an empty traversal.

## Extra Insights

### 💡 Optimization Thinking

* Comparisons such as `num < 0` are cheaper than modulo operations like `num % 3 == 0`.
* Writing:

  ```python
  if num < 0 and num % 3 == 0:
  ```

  allows Python's short-circuit evaluation to skip the modulo operation for positive numbers.

### 🧠 Short-Circuit Evaluation

* Python evaluates `and` from left to right.
* If the first condition is `False`, the remaining conditions are not evaluated.
* Ordering conditions intelligently can avoid unnecessary work.

### 🎯 Edge Cases Matter

* Always think about:

  * Empty lists
  * No matching elements
  * Only one matching element
* Sometimes these cases are handled naturally by the algorithm without writing extra code.

### 🚀 Milestone Achieved

* Completed **50 out of 100** logic-building problems.
* Strong understanding of:

  * Counting
  * Summation
  * Maximum and minimum tracking
  * First and last occurrence
  * Index tracking
  * Multiple filtering conditions
  * One-pass and two-pass algorithms
  * Pattern recognition
