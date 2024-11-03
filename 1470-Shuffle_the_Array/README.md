# Shuffle the Array

## Problem Statement
Given an array `nums` consisting of `2n` elements in the form `[x1, x2, ..., xn, y1, y2, ..., yn]`, return the array in the form `[x1, y1, x2, y2, ..., xn, yn]`.

## Examples

### Example 1:
**Input**:  
`nums = [2, 5, 1, 3, 4, 7]`, `n = 3`  
**Output**:  
`[2, 3, 5, 4, 1, 7]`  
**Explanation**:  
Given `x1 = 2`, `x2 = 5`, `x3 = 1`, `y1 = 3`, `y2 = 4`, `y3 = 7`, the array is returned as `[2, 3, 5, 4, 1, 7]`.

### Example 2:
**Input**:  
`nums = [1, 2, 3, 4, 4, 3, 2, 1]`, `n = 4`  
**Output**:  
`[1, 4, 2, 3, 3, 2, 4, 1]`

### Example 3:
**Input**:  
`nums = [1, 1, 2, 2]`, `n = 2`  
**Output**:  
`[1, 2, 1, 2]`

## Constraints:
- `1 <= n <= 500`
- `nums.length == 2 * n`
- `1 <= nums[i] <= 10^3`

## Approach:
1. Split `nums` into two halves: the first half for `x` values and the second half for `y` values.
2. Iterate through the range `0` to `n - 1` and combine elements from both halves alternatively to create the shuffled array.
3. Return the resulting array.

## Complexity Analysis:
- **Time Complexity**: `O(n)`, where `n` is the length of the `x` or `y` half of `nums` (i.e., `n = nums.length / 2`).
- **Space Complexity**: `O(n)` for the output array.


