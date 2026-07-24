# Day 14

## Problem 61

* **Concept:** Count Negative Numbers Greater Than Target
* **Time Complexity:** O(n)
* **Space Complexity:** O(1)
* **Lesson Learned:** Combined multiple conditions (`negative` and `greater than target`) while counting in a single traversal.

---

## Problem 62

* **Concept:** Sum of Positive Odd Numbers Less Than Target
* **Time Complexity:** O(n)
* **Space Complexity:** O(1)
* **Lesson Learned:** Practiced combining multiple filtering conditions while accumulating a sum.

---

## Problem 63

* **Concept:** Closest Number to Zero
* **Time Complexity:** O(n)
* **Space Complexity:** O(1)
* **Lesson Learned:**

  * Compared transformed values using `abs()`.
  * Returned the original value instead of the transformed one.
  * Implemented tie-breaking by preferring the positive number when two values are equally close to zero.

---

## Problem 64

* **Concept:** Most Frequent Negative Number
* **Time Complexity:** O(n)
* **Space Complexity:** O(n)
* **Lesson Learned:**

  * Used a dictionary (`dict`) to count frequencies.
  * Learned frequency counting with hash maps.
  * Understood tie-breaking when multiple elements have the same highest frequency.
  * Compared my multi-step solution with an interview-style optimized solution.

---

## Problem 65

* **Concept:** First Repeating Positive Number
* **Time Complexity:** O(n)
* **Space Complexity:** O(n)
* **Lesson Learned:**

  * Used a hash map to detect repeated elements.
  * Learned that a `set` is more suitable than a dictionary when only existence needs to be tracked.
  * Understood the difference between choosing the right data structure (`dict` vs `set`).

---

# Extra Insights

## 🔹 Comparing Transformed Values

Sometimes the comparison is performed on a transformed value (`abs(num)`), while the returned answer remains the original value.

---

## 🔹 Tie-Breaking

Many interview problems require handling ties explicitly.

Examples:

* Equal distance from zero → choose the positive number.
* Equal frequency → choose the larger number.

---

## 🔹 Dictionaries vs Sets

Use a **dictionary (`dict`)** when:

* You need to store extra information (frequency, index, count, etc.).

Use a **set** when:

* You only need to know whether an element has already been seen.

---

## 🔹 Time Complexity Reminder

For Python dictionaries and sets:

* Lookup → **O(1)** average
* Insertion → **O(1)** average
* Worst-case (hash collisions) → **O(n)**, but interviews assume average-case complexity.

---

# Milestone

Today marked the transition from solving repetitive logic problems to solving problems that required:

* Choosing the correct data structure.
* Designing comparison rules.
* Handling tie-breaking conditions.
* Thinking about algorithm design instead of only writing loops.

**Progress:** **65 / 100 Problems Completed** 🚀
