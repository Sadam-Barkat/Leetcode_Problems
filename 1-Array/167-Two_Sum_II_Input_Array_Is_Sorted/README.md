# Two Sum II - Input Array Is Sorted

## Problem Description

Given a 1-indexed array of integers `numbers` that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Return the indices of the two numbers, `index1` and `index2`, where `1 <= index1 < index2 <= numbers.length`, as an integer array `[index1, index2]` of length 2.

The solution must use only constant extra space.

### Constraints:
- `2 <= numbers.length <= 3 * 10^4`
- `-1000 <= numbers[i] <= 1000`
- `numbers` is sorted in non-decreasing order.
- `-1000 <= target <= 1000`
- The tests are generated such that there is exactly one solution.

## Example 1:
**Input:**
```python
numbers = [2, 7, 11, 15]
target = 9
