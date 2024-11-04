# Squares of a Sorted Array

## Problem Statement
Given an integer array `nums` sorted in non-decreasing order, return an array of the squares of each number, also sorted in non-decreasing order.

### Example 1
- **Input**: `nums = [-4, -1, 0, 3, 10]`
- **Output**: `[0, 1, 9, 16, 100]`
- **Explanation**: After squaring, the array becomes `[16, 1, 0, 9, 100]`. After sorting, it becomes `[0, 1, 9, 16, 100]`.

### Example 2
- **Input**: `nums = [-7, -3, 2, 3, 11]`
- **Output**: `[4, 9, 9, 49, 121]`

## Constraints
- `1 <= nums.length <= 10^4`
- `-10^4 <= nums[i] <= 10^4`
- `nums` is sorted in non-decreasing order.

## Approach
1. **Squaring and Sorting**:
   - Iterate through the array, square each element.
   - Use an efficient sorting algorithm to sort the squared elements.

2. **Optimal Two-Pointer Approach**:
   - Start with two pointers at both ends of the array.
   - Compare and place the larger squared value at the end of the result array.
   - Move the pointer inward accordingly.


