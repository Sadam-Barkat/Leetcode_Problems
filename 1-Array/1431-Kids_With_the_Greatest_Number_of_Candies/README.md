# Kids With the Greatest Number of Candies

## Problem Statement
Given an integer array `candies`, where `candies[i]` represents the number of candies the ith kid has, and an integer `extraCandies`, determine if after giving the ith kid all the extra candies, they will have the greatest number of candies among all the kids. Return a boolean array `result` of length `n`, where `result[i]` is `true` if they have the greatest number of candies, or `false` otherwise.

## Example

### Input
- `candies = [2, 3, 5, 1, 3]`
- `extraCandies = 3`

### Output
- `[true, true, true, false, true]`

### Explanation
- Kid 1 will have `2 + 3 = 5` candies (greatest).
- Kid 2 will have `3 + 3 = 6` candies (greatest).
- Kid 3 will have `5 + 3 = 8` candies (greatest).
- Kid 4 will have `1 + 3 = 4` candies (not the greatest).
- Kid 5 will have `3 + 3 = 6` candies (greatest).

## Constraints
- `n == candies.length`
- `2 <= n <= 100`
- `1 <= candies[i] <= 100`
- `1 <= extraCandies <= 50`

## Approach
- Find the maximum number of candies any child currently has.
- Iterate through the array and check if adding `extraCandies` allows each child to meet or exceed this maximum.
- Return the results as a boolean array.

## Result
The solution helps identify which kids can have the most candies when given the extra candies.
