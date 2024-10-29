# Remove Duplicates from Sorted Array

## Problem Description
Given a sorted integer array `nums`, remove duplicates **in-place** such that each unique element appears only once, keeping their relative order. 

Return the number of unique elements `k` and modify the array so that the first `k` elements of `nums` contain the unique elements in the order they appeared initially. Elements after the first `k` elements are not important.

### Examples

**Example 1:**
- Input: `nums = [1,1,2]`
- Output: `2, nums = [1,2,_]`

**Example 2:**
- Input: `nums = [0,0,1,1,1,2,2,3,3,4]`
- Output: `5, nums = [0,1,2,3,4,_,_,_,_,_]`

### Constraints
- `1 <= nums.length <= 30,000`
- `-100 <= nums[i] <= 100`
- `nums` is sorted in non-decreasing order.

## Approach
1. Use two pointers to traverse and update `nums`:
   - One pointer iterates through the list, and the other tracks the last position of unique elements.
2. For each unique element encountered, place it at the current position tracked by the second pointer, then increment the pointer.
3. Return `k`, representing the number of unique elements.

