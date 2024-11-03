# Maximum Water Container Problem

## Problem Statement
You are given an integer array `height` of length `n`, where `n` represents vertical lines drawn on an x-axis. The two endpoints of the `ith` line are at coordinates `(i, 0)` and `(i, height[i])`.

The task is to find two lines that, along with the x-axis, form a container that holds the maximum amount of water. The container must be upright and cannot be slanted.

## Example 1:
**Input**: `height = [1,8,6,2,5,4,8,3,7]`  
**Output**: `49`  
**Explanation**: The vertical lines are represented by the array `[1,8,6,2,5,4,8,3,7]`. The maximum area of water the container can hold is `49`.

## Example 2:
**Input**: `height = [1,1]`  
**Output**: `1`  
**Explanation**: The maximum area that can be contained between the two lines is `1`.

## Constraints:
- `n == height.length`
- `2 <= n <= 10^5`
- `0 <= height[i] <= 10^4`

## Approach:
1. Use a two-pointer technique:
   - Start with one pointer at the beginning (`left`) and the other at the end (`right`) of the array.
   - Calculate the area between the lines pointed to by `left` and `right`.
   - Move the pointer pointing to the shorter line inward to potentially find a larger container.
   - Continue until the pointers meet.

2. The maximum area found during these iterations is the answer.

## Complexity:
- **Time Complexity**: `O(n)`, where `n` is the number of elements in `height`.
- **Space Complexity**: `O(1)`, as no additional space is used except for variables to store the maximum area.

