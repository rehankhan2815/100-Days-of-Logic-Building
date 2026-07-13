# Day 4

## Problem 11

* **Concept:** Smallest Positive Number
* **Time Complexity:** O(n)
* **Space Complexity:** O(1)
* **Lesson Learned:** Tracking problems require the tracking variable to be initialized **before** the loop so it remembers previous values. Sentinel values like `math.inf` help handle minimum-finding problems.

## Problem 12

* **Concept:** Index of the First Negative Number
* **Time Complexity:** O(n)
* **Space Complexity:** O(1)
* **Lesson Learned:** When the problem asks for an index, iterate using indices instead of values. Use the Early Return pattern to stop as soon as the answer is found.

## Problem 13

* **Concept:** Check if All Numbers are Positive
* **Time Complexity:** O(n)
* **Space Complexity:** O(1)
* **Lesson Learned:** Many boolean problems are just search problems in disguise. Return `False` immediately when a negative number is found; otherwise return `True` after the loop completes.

## Bonus Learning

* **Concept:** Pattern Recognition
* **Lesson Learned:** Different questions can share the same underlying logic. Changing only the return value or condition often transforms one problem into another.
