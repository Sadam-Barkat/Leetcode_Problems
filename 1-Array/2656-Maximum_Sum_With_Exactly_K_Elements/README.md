# Maximize Score by Performing K Operations

## Problem Statement
You are given a 0-indexed integer array `nums` and an integer `k`. Your task is to perform the following operation exactly `k` times in order to maximize your score:

1. Select an element `m` from `nums`.
2. Remove the selected element `m` from the array.
3. Add a new element with a value of `m + 1` to the array.
4. Increase your score by `m`.

Return the maximum score you can achieve after performing the operation exactly `k` times.

---

### Example 1:
**Input:**  
`nums = [1, 2, 3, 4, 5]`, `k = 3`  
**Output:**  
`18`  

**Explanation:**  
- Select `5`. Score: `5`, `nums = [1, 2, 3, 4, 6]`.  
- Select `6`. Score: `5 + 6 = 11`, `nums = [1, 2, 3, 4, 7]`.  
- Select `7`. Score: `5 + 6 + 7 = 18`, `nums = [1, 2, 3, 4, 8]`.  

The maximum score is `18`.

---

### Example 2:
**Input:**  
`nums = [5, 5, 5]`, `k = 2`  
**Output:**  
`11`  

**Explanation:**  
- Select `5`. Score: `5`, `nums = [5, 5, 6]`.  
- Select `6`. Score: `5 + 6 = 11`, `nums = [5, 5, 7]`.  

The maximum score is `11`.

---

### Constraints:
- `1 <= nums.length <= 100`
- `1 <= nums[i] <= 100`
- `1 <= k <= 100`


