# Three Sum Problem

## Problem Description
Given an integer array `nums`, return all unique triplets `[nums[i], nums[j], nums[k]]` such that:
- `i != j`, `i != k`, and `j != k`
- `nums[i] + nums[j] + nums[k] == 0`

The solution set must not contain duplicate triplets.

## Examples
### Example 1
Input: `nums = [-1, 0, 1, 2, -1, -4]`  
Output: `[[-1, -1, 2], [-1, 0, 1]]`  
Explanation:  
- Triplets like `[-1, 0, 1]` and `[-1, -1, 2]` sum up to `0` and are unique in the output.

### Example 2
Input: `nums = [0, 1, 1]`  
Output: `[]`  
Explanation:  
- No triplet sums up to `0`.

### Example 3
Input: `nums = [0, 0, 0]`  
Output: `[[0, 0, 0]]`  
Explanation:  
- The only triplet `[0, 0, 0]` sums to `0`.

## Constraints
- `3 <= nums.length <= 3000`
- `-10^5 <= nums[i] <= 10^5`

## Solution Approach
1. **Sorting**: First, sort the array `nums`. This allows us to use the two-pointer technique to find triplets.
2. **Two-pointer Technique**: For each element `nums[i]`, use two pointers (`left` and `right`) to find pairs that sum to `-nums[i]`.
3. **Avoid Duplicates**: Skip duplicate elements to avoid duplicate triplets in the result.
4. **Complexity**: The time complexity is `O(n^2)` due to the nested loops, and the space complexity is `O(n)` for storing results.

## Usage
This solution is commonly used in coding interviews to test understanding of sorting, two-pointer techniques, and duplicate handling in arrays.
