# Rank Transform of an Array

## Problem Description

Given an array of integers `arr`, replace each element with its rank.

### Rank Rules:
1. Rank is an integer starting from `1`.
2. The larger the element, the larger the rank.
3. If two elements are equal, their rank must be the same.
4. Ranks should be as small as possible.

---

## Examples

### Example 1:
**Input:**  
`arr = [40,10,20,30]`  
**Output:**  
`[4,1,2,3]`  

**Explanation:**  
- `40` is the largest element → Rank `4`.  
- `10` is the smallest element → Rank `1`.  
- `20` is the second smallest element → Rank `2`.  
- `30` is the third smallest element → Rank `3`.

---

### Example 2:
**Input:**  
`arr = [100,100,100]`  
**Output:**  
`[1,1,1]`  

**Explanation:**  
All elements are the same, so they share the same rank.

---

### Example 3:
**Input:**  
`arr = [37,12,28,9,100,56,80,5,12]`  
**Output:**  
`[5,3,4,2,8,6,7,1,3]`

---

## Constraints

1. `0 <= arr.length <= 10^5`
2. `-10^9 <= arr[i] <= 10^9`
