# Majority Element

## Problem Description

Given an array `nums` of size `n`, return the **majority element**.

The majority element is the element that appears more than `⌊n / 2⌋` times. You can assume that the majority element **always exists** in the array.

---

## Examples

### Example 1:
**Input**:  
`nums = [3, 2, 3]`  

**Output**:  
`3`  

**Explanation**:  
The element `3` appears more than `⌊3 / 2⌋ = 1` times, so it is the majority element.

---

### Example 2:
**Input**:  
`nums = [2, 2, 1, 1, 1, 2, 2]`  

**Output**:  
`2`  

**Explanation**:  
The element `2` appears `4` times, which is more than `⌊7 / 2⌋ = 3`. Thus, `2` is the majority element.

---

## Constraints

- `n == nums.length`
- `1 <= n <= 5 * 10^4`
- `-10^9 <= nums[i] <= 10^9`

