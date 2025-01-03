# Longest Consecutive Sequence

## Problem Description

Given an unsorted array of integers `nums`, return the length of the longest consecutive elements sequence.

Your algorithm should run in **O(n)** time complexity.

### Examples

#### Example 1:
**Input:** 
```python
nums = [100,4,200,1,3,2]
Output:

python
Copy code
4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore, its length is 4.

Example 2:
Input:

python
Copy code
nums = [0,3,7,2,5,8,4,6,0,1]
Output:

python
Copy code
9
Explanation: The longest consecutive elements sequence is [0, 1, 2, 3, 4, 5, 6, 7, 8]. Therefore, its length is 9.

Constraints:
0 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9