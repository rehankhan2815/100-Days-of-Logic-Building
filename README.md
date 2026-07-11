# Day 1

## Problem 1
- Concept: Finding Largest Element
- Time Complexity: O(n)
- Space Complexity: O(1)
- Lesson Learned: Initialize with a valid element.

## Problem 2
- Concept: Second Largest Element
- Time Complexity: O(n)
- Space Complexity: O(1)
- Lesson Learned: Initialization matters.

## Problem 3
- Concept: Check if Array is Sorted
- Time Complexity: O(n)
- Space Complexity: O(1)
- Lesson Learned: Early exit improves efficiency.

# Day 2 - Logic Building Journey

## Problems Solved

### Problem 4 - Count Positive Numbers
**Concept:** Counting Pattern

**Algorithm:**
1. Initialize a counter to 0.
2. Traverse the list.
3. If the current number is positive, increment the counter.
4. Return the counter.

**Time Complexity:** O(n)

**Space Complexity:** O(1)

**Lesson Learned:**
- Counting problems usually start with a counter initialized to 0.
- The algorithm remains the same; only the condition changes.

---

### Problem 5 - Count Even and Odd Numbers
**Concept:** Multiple Counters

**Algorithm:**
1. Initialize `even` and `odd` to 0.
2. Traverse the list.
3. If the number is even, increment `even`; otherwise increment `odd`.
4. Return both counts.

**Time Complexity:** O(n)

**Space Complexity:** O(1)

**Lesson Learned:**
- Multiple counters can be maintained in a single traversal.
- Meaningful variable names improve readability.

---

### Problem 6 - Sum of Positive Numbers
**Concept:** Accumulation Pattern

**Algorithm:**
1. Initialize `total` to 0.
2. Traverse the list.
3. Add the number to `total` if it is positive.
4. Return `total`.

**Time Complexity:** O(n)

**Space Complexity:** O(1)

**Lesson Learned:**
- Accumulation is similar to counting, but instead of adding 1, we add the value itself.

---

### Bonus Learning - Largest Even Number

**New Concept:** Sentinel Values

**Lesson Learned:**
- Use `None` to represent "no valid value found yet."
- Before comparing, check whether a valid value has already been assigned.
- This technique appears frequently in interview problems.