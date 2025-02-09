# 2364. Count Number of Bad Pairs

## Problem Statement

You are given a **0-indexed** integer array `nums`. A pair of indices `(i, j)` is a **bad pair** if:

\[
i < j \quad \text{and} \quad j - i \neq nums[j] - nums[i]
\]

Return the **total number of bad pairs** in `nums`.

---

## Examples

### Example 1:
**Input:**  
```plaintext
nums = [4,1,3,3]
Output:

plaintext
Copy
Edit
5
Explanation:

The bad pairs are: (0,1), (0,2), (0,3), (1,2), and (2,3).
Therefore, the total number of bad pairs is 5.
Example 2:
Input:

plaintext
Copy
Edit
nums = [1,2,3,4,5]
Output:

plaintext
Copy
Edit
0
Explanation:

There are no bad pairs since for all (i, j), j - i == nums[j] - nums[i].
Constraints
1
≤
nums.length
≤
10
5
1≤nums.length≤10 
5
 
1
≤
nums
[
𝑖
]
≤
10
9
1≤nums[i]≤10 
9