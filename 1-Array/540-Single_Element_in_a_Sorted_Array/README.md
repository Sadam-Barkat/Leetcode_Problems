# Find Single Element in a Sorted Array

## Problem Statement
You are given a sorted array of integers where every element appears exactly twice, except for one element, which appears only once.

Your task is to find the single element that appears only once in the array.

### Requirements
- **Time Complexity:** O(log n)
- **Space Complexity:** O(1)

---

## Examples

### Example 1
**Input:**  
`nums = [1,1,2,3,3,4,4,8,8]`  

**Output:**  
`2`  

**Explanation:**  
In the array, every element appears twice except for `2`, which appears only once.

### Example 2
**Input:**  
`nums = [3,3,7,7,10,11,11]`  

**Output:**  
`10`  

**Explanation:**  
In the array, every element appears twice except for `10`, which appears only once.

---

## Constraints
1. `1 <= nums.length <= 10^5`  
2. `0 <= nums[i] <= 10^5`  
3. The input array is sorted in non-decreasing order.

