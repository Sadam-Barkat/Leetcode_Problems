# Find Target Indices After Sorting Array

## Problem Statement
You are given a 0-indexed integer array `nums` and a target element `target`. A target index is an index `i` such that `nums[i] == target`.

Your task is to:
1. Sort the array `nums` in non-decreasing order.
2. Return a list of all target indices in the sorted array.
3. If there are no target indices, return an empty list.

The returned list must be sorted in increasing order.

---

### Example 1:
**Input:**  
`nums = [1, 2, 5, 2, 3]`, `target = 2`  
**Output:**  
`[1, 2]`  

**Explanation:**  
After sorting, `nums = [1, 2, 2, 3, 5]`.  
The indices where `nums[i] == 2` are `1` and `2`.

---

### Example 2:
**Input:**  
`nums = [1, 2, 5, 2, 3]`, `target = 3`  
**Output:**  
`[3]`  

**Explanation:**  
After sorting, `nums = [1, 2, 2, 3, 5]`.  
The index where `nums[i] == 3` is `3`.

---

### Example 3:
**Input:**  
`nums = [1, 2, 5, 2, 3]`, `target = 5`  
**Output:**  
`[4]`  

**Explanation:**  
After sorting, `nums = [1, 2, 2, 3, 5]`.  
The index where `nums[i] == 5` is `4`.

---

### Constraints:
- `1 <= nums.length <= 100`
- `1 <= nums[i], target <= 100`
