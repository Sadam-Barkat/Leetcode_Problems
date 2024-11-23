# Single Number II

## Problem Description

Given an integer array `nums`, where every element appears three times except for one which appears exactly once. Your task is to find that single element and return it.

You must implement a solution with:
- **Linear runtime complexity** (O(n)).
- **Constant extra space** (O(1)).

## Example 1

**Input:**  
`nums = [2, 2, 3, 2]`

**Output:**  
`3`

## Example 2

**Input:**  
`nums = [0, 1, 0, 1, 0, 1, 99]`

**Output:**  
`99`

## Constraints
- `1 <= nums.length <= 3 * 10^4`
- `-2^31 <= nums[i] <= 2^31 - 1`
- Each element in `nums` appears exactly three times except for one element which appears once.
