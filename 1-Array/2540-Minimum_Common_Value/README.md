# Minimum Common Integer in Two Sorted Arrays

## Problem Description

Given two integer arrays `nums1` and `nums2`, sorted in non-decreasing order, return the **minimum integer common to both arrays**. If there is no common integer amongst `nums1` and `nums2`, return `-1`.

An integer is considered common to `nums1` and `nums2` if it appears in both arrays at least once.

---

## Examples

### Example 1:
**Input**:  
`nums1 = [1, 2, 3]`  
`nums2 = [2, 4]`  

**Output**:  
`2`  

**Explanation**:  
The smallest element common to both arrays is `2`, so we return `2`.

---

### Example 2:
**Input**:  
`nums1 = [1, 2, 3, 6]`  
`nums2 = [2, 3, 4, 5]`  

**Output**:  
`2`  

**Explanation**:  
There are two common elements, `2` and `3`. Out of these, `2` is the smallest, so we return `2`.

---

## Constraints

- `1 <= nums1.length, nums2.length <= 10^5`
- `1 <= nums1[i], nums2[j] <= 10^9`
- Both `nums1` and `nums2` are sorted in **non-decreasing order**.

