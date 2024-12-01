# Find Final Value of Original in an Array

## Problem Description

You are given an array of integers `nums` and an integer `original`. The task is to perform the following steps iteratively:

1. Check if `original` exists in `nums`.
2. If it does, multiply `original` by 2 (i.e., `original = 2 * original`).
3. Repeat the process with the updated `original` as long as it is found in `nums`.
4. If `original` is not found in `nums`, stop and return the current value of `original`.

### Example 1

**Input:**  
`nums = [5,3,6,1,12]`, `original = 3`  

**Output:**  
`24`  

**Explanation:**  
- `3` is found in `nums`. Multiply `3` by 2 to get `6`.  
- `6` is found in `nums`. Multiply `6` by 2 to get `12`.  
- `12` is found in `nums`. Multiply `12` by 2 to get `24`.  
- `24` is not found in `nums`. Return `24`.  

### Example 2

**Input:**  
`nums = [2,7,9]`, `original = 4`  

**Output:**  
`4`  

**Explanation:**  
- `4` is not found in `nums`. Return `4`.  

## Constraints

- `1 <= nums.length <= 1000`
- `1 <= nums[i], original <= 1000`

## Usage

This problem is often encountered in scenarios where you need to iteratively search and modify a value based on certain conditions in a dataset. It has applications in simulation, iterative computations, and problem-solving frameworks.
