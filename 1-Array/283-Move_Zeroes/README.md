# Move Zeroes to End of Array

## Problem Description
Given an integer array `nums`, move all `0`s to the end of the array while maintaining the relative order of the non-zero elements. The operation must be done **in-place** without creating a copy of the array.

### Examples

**Example 1:**
- Input: `nums = [0,1,0,3,12]`
- Output: `[1,3,12,0,0]`

**Example 2:**
- Input: `nums = [0]`
- Output: `[0]`

### Constraints
- `1 <= nums.length <= 10^4`
- `-2^31 <= nums[i] <= 2^31 - 1`

## Approach
1. Use two pointers: one to iterate through the array and another to keep track of the position for non-zero elements.
2. As you iterate, whenever a non-zero is found, swap it with the element at the position of the second pointer, then move the pointer.
3. After completing the iteration, all non-zero elements will be at the start, and the remaining positions will be `0`.

