# Find All Numbers Disappeared in an Array

## Problem Description
Given an array `nums` of `n` integers where `nums[i]` is in the range `[1, n]`, return an array of all the integers in the range `[1, n]` that do not appear in `nums`.

---

## Examples

### Example 1
**Input**:  
```plaintext
nums = [4,3,2,7,8,2,3,1]
Output:

plaintext
Copy code
[5,6]
Explanation:
The numbers 5 and 6 are missing from the range [1, 8].

Example 2
Input:

plaintext
Copy code
nums = [1,1]
Output:

plaintext
Copy code
[2]
Explanation:
The number 2 is missing from the range [1, 2].

Constraints
n == nums.length
1 <= n <= 10^5
1 <= nums[i] <= n