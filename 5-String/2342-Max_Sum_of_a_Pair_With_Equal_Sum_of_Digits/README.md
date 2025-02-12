# Maximum Sum of Pairs with Equal Digit Sum

## Problem Statement
Given a list of integers `nums`, find the maximum sum of any two numbers that have the same digit sum. If no such pair exists, return `-1`.

## Approach
- **Calculate Digit Sum:** Convert each number to a string, map its digits to integers, and sum them.
- **Use a Dictionary:** Store the maximum number encountered for each digit sum.
- **Find Maximum Pair:** If a digit sum appears more than once, update the maximum sum.

## Complexity Analysis
- **Time Complexity:** `O(n)`, as we iterate through the list once.
- **Space Complexity:** `O(n)`, for storing numbers in the dictionary.

## Example
```python
nums = [51, 71, 17, 42]
solution = Solution()
print(solution.maximumSum(nums))  # Output: 93
