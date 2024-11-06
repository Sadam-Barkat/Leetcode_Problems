# Duplicate Check in Array

## Problem Description
Given an integer array `nums`, the goal is to determine if any value appears at least twice in the array. If any element is repeated, return `true`; otherwise, return `false`.

## Examples

### Example 1
- **Input**: `nums = [1, 2, 3, 1]`
- **Output**: `true`
- **Explanation**: The element `1` occurs twice (at indices `0` and `3`).

### Example 2
- **Input**: `nums = [1, 2, 3, 4]`
- **Output**: `false`
- **Explanation**: All elements are distinct.

### Example 3
- **Input**: `nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]`
- **Output**: `true`
- **Explanation**: There are multiple repeated elements, including `1`, `3`, and `4`.

## Constraints
- \(1 \leq \text{nums.length} \leq 10^5\)
- \(-10^9 \leq \text{nums[i]} \leq 10^9\)

