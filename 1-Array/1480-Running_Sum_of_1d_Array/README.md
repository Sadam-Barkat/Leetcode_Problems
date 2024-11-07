# Running Sum of 1d Array

## Problem Statement
Given an array `nums`, we define a running sum of the array as `runningSum[i] = sum(nums[0]…nums[i])`. The task is to return the running sum of `nums`.

## Example 1:
**Input**: `nums = [1, 2, 3, 4]`  
**Output**: `[1, 3, 6, 10]`  
**Explanation**: The running sum is calculated as follows:
- `runningSum[0] = 1`
- `runningSum[1] = 1 + 2 = 3`
- `runningSum[2] = 1 + 2 + 3 = 6`
- `runningSum[3] = 1 + 2 + 3 + 4 = 10`

## Example 2:
**Input**: `nums = [1, 1, 1, 1, 1]`  
**Output**: `[1, 2, 3, 4, 5]`  
**Explanation**: The running sum is calculated as `[1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1]`.

## Example 3:
**Input**: `nums = [3, 1, 2, 10, 1]`  
**Output**: `[3, 4, 6, 16, 17]`  
**Explanation**: The running sum is `[3, 3+1, 3+1+2, 3+1+2+10, 3+1+2+10+1]`.

## Constraints:
- `1 <= nums.length <= 1000`
- `-10^6 <= nums[i] <= 10^6`

## Approach:
1. Initialize an empty array `runningSum` or modify `nums` directly.
2. Iterate through the `nums` array starting from the second element.
3. For each element `i`, update `nums[i]` by adding `nums[i-1]` to it to get the cumulative sum.
4. Return the modified `nums` array or the `runningSum` array.

## Complexity:
- **Time Complexity**: `O(n)`, where `n` is the number of elements in `nums`.
- **Space Complexity**: `O(1)` if modifying the input array directly, otherwise `O(n)` for a new array.


