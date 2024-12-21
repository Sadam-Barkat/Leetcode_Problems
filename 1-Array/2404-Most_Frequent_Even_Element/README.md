# Most Frequent Even Element

## Problem Description

Given an integer array `nums`, the task is to return the most frequent even element. 

- If there is a tie (i.e., multiple even elements with the same frequency), return the smallest even element.
- If there are no even elements in the array, return `-1`.

### Example 1:
**Input:**
```python
nums = [0, 1, 2, 2, 4, 4, 1]
Output:

python
Copy code
2
Explanation: The even elements are 0, 2, and 4. Both 2 and 4 appear the most, but since 2 is smaller, it is returned.

Example 2:
Input:

python
Copy code
nums = [4, 4, 4, 9, 2, 4]
Output:

python
Copy code
4
Explanation: The even element 4 appears the most, so 4 is returned.

Example 3:
Input:

python
Copy code
nums = [29, 47, 21, 41, 13, 37, 25, 7]
Output:

python
Copy code
-1
Explanation: There are no even elements in the array, so -1 is returned.

Constraints
1 <= nums.length <= 2000
0 <= nums[i] <= 10^5