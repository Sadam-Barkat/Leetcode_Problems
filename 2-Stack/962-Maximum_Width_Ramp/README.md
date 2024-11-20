# Maximum Width Ramp

## Problem Description

A **ramp** in an integer array `nums` is a pair `(i, j)` for which:
- `i < j`
- `nums[i] <= nums[j]`

The **width** of such a ramp is defined as `j - i`.

Given an integer array `nums`, the task is to return the **maximum width** of a ramp in `nums`. If there is no ramp, return `0`.

---

## Examples

### Example 1:
- **Input:** `nums = [6, 0, 8, 2, 1, 5]`
- **Output:** `4`
- **Explanation:** The maximum width ramp is achieved at `(i, j) = (1, 5)` where `nums[1] = 0` and `nums[5] = 5`.

### Example 2:
- **Input:** `nums = [9, 8, 1, 0, 1, 9, 4, 0, 4, 1]`
- **Output:** `7`
- **Explanation:** The maximum width ramp is achieved at `(i, j) = (2, 9)` where `nums[2] = 1` and `nums[9] = 1`.

---

## Constraints:
- `2 <= nums.length <= 5 * 10⁴`
- `0 <= nums[i] <= 5 * 10⁴`

---

## Approach Using Stack

1. **Monotonic Decreasing Stack**:
   - Maintain a stack of indices where the values in `nums` are in decreasing order.
   - Traverse the array from left to right to build the stack.

2. **Calculate Maximum Width**:
   - Traverse the array from right to left.
   - Pop indices from the stack while the current value is greater than or equal to the value at the index on top of the stack.
   - Compute the ramp width for each valid pair and keep track of the maximum.

---

## Complexity
- **Time Complexity:** \(O(n)\)  
  - Building the stack takes \(O(n)\), and finding the maximum ramp also takes \(O(n)\).
- **Space Complexity:** \(O(n)\)  
  - The stack stores at most \(n\) indices.
