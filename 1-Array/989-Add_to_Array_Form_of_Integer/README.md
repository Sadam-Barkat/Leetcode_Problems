# Array Form of Integer + k

This repository contains a solution to the problem of adding a number (given as an array-form integer) and a regular integer `k`. The goal is to return the array-form of the sum.

## Problem Description

You are given two inputs:

1. An integer `num` represented as an array where each element corresponds to a digit of the number. The array is in left-to-right order.
2. An integer `k`.

You need to return the array-form of the integer `num + k`.

### Example 1

**Input:**  
`num = [1,2,0,0]`, `k = 34`

**Output:**  
`[1,2,3,4]`

**Explanation:**  
1200 + 34 = 1234

### Example 2

**Input:**  
`num = [2,7,4]`, `k = 181`

**Output:**  
`[4,5,5]`

**Explanation:**  
274 + 181 = 455

### Example 3

**Input:**  
`num = [2,1,5]`, `k = 806`

**Output:**  
`[1,0,2,1]`

**Explanation:**  
215 + 806 = 1021

## Constraints

- `1 <= num.length <= 10^4`
- `0 <= num[i] <= 9`
- `num` does not contain any leading zeros except for the zero itself.
- `1 <= k <= 10^4`