# 16. 3Sum Closest

## Problem Description
Given an integer array `nums` of length `n` and an integer `target`, find three integers in `nums` such that the sum is closest to `target`. Return the sum of the three integers. You may assume that each input would have exactly one solution.

### Constraints
- `3 <= nums.length <= 500`
- `-1000 <= nums[i] <= 1000`
- `-10^4 <= target <= 10^4`

## Input
- `nums`: An array of integers.
- `target`: An integer representing the target sum.

## Output
- An integer representing the sum of three integers closest to the target.

## Example

### Example 1:
#### Input:
nums = [-1, 2, 1, -4], target = 1

shell
Copy code

#### Output:
2

markdown
Copy code

#### Explanation:
The sum that is closest to the target is `2` (i.e., `-1 + 2 + 1 = 2`).

## Approach
1. Sort the array to use the two-pointer approach effectively.
2. Iterate through the array, fixing one element at a time.
3. Use two pointers to find the closest sum for the remaining part of the array.
4. Keep track of the closest sum during each iteration.

## Complexity
- **Time Complexity:** O(n²), where `n` is the length of the array. Sorting takes O(n log n), and for each fixed element, the two-pointer traversal takes O(n).
- **Space Complexity:** O(1), as no additional data structures are used.