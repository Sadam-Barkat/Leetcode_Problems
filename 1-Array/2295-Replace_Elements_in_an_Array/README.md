# 2295. Replace Elements in an Array

## Problem Description
You are given a **0-indexed** array `nums` that consists of `n` distinct positive integers. You are also given a 2D integer array `operations`, where `operations[i] = [oldValue, newValue]` indicates that you should replace the value `oldValue` with `newValue` in `nums`.

- After performing all the operations, return the array `nums`.

## Example 1:
**Input:**  
`nums = [1, 2, 4, 6]`  
`operations = [[1, 3], [4, 7], [6, 1]]`

**Output:**  
`[3, 2, 7, 1]`

**Explanation:**  
- Replace `1` with `3`: `nums = [3, 2, 4, 6]`
- Replace `4` with `7`: `nums = [3, 2, 7, 6]`
- Replace `6` with `1`: `nums = [3, 2, 7, 1]`

## Example 2:
**Input:**  
`nums = [1, 2]`  
`operations = [[1, 3], [2, 1], [3, 2]]`

**Output:**  
`[2, 1]`

**Explanation:**  
- Replace `1` with `3`: `nums = [3, 2]`
- Replace `2` with `1`: `nums = [3, 1]`
- Replace `3` with `2`: `nums = [2, 1]`

## Constraints:
- `n == nums.length`
- `1 <= n, operations.length <= 10^5`
- All values in `nums` are distinct.
- Each `operations[i] = [oldValue, newValue]` contains distinct values.
- `oldValue` exists in `nums`.


