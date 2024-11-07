# How Many Numbers Are Smaller Than the Current Number

## Problem Statement
Given an array `nums`, for each element `nums[i]`, find out how many numbers in the array are smaller than it. For each `nums[i]`, count the number of valid `j`'s such that `j != i` and `nums[j] < nums[i]`.

Return the result as an array.

## Examples

### Example 1
**Input**: 
- `nums = [8, 1, 2, 2, 3]`

**Output**: 
- `[4, 0, 1, 1, 3]`

**Explanation**:
- For `nums[0] = 8`, there are 4 numbers smaller than it: `1, 2, 2, 3`.
- For `nums[1] = 1`, no numbers are smaller.
- For `nums[2] = 2`, there is 1 number smaller: `1`.
- For `nums[3] = 2`, there is 1 number smaller: `1`.
- For `nums[4] = 3`, there are 3 numbers smaller: `1, 2, 2`.

### Example 2
**Input**:
- `nums = [6, 5, 4, 8]`

**Output**:
- `[2, 1, 0, 3]`

**Explanation**:
- For `nums[0] = 6`, there are 2 numbers smaller: `5, 4`.
- For `nums[1] = 5`, there is 1 number smaller: `4`.
- For `nums[2] = 4`, no numbers are smaller.
- For `nums[3] = 8`, there are 3 numbers smaller: `6, 5, 4`.

### Example 3
**Input**:
- `nums = [7, 7, 7, 7]`

**Output**:
- `[0, 0, 0, 0]`

**Explanation**:
- No number is smaller than any other in the array as all are equal.

## Constraints
- `2 <= nums.length <= 500`
- `0 <= nums[i] <= 100`

## Approach
- Use a nested loop approach to compare each element `nums[i]` with every other element `nums[j]`.
- Count the number of times `nums[j]` is less than `nums[i]` for all `j` where `j != i`.
- Construct the result array based on these counts.

## Result
The solution effectively counts how many numbers are smaller than each element in `nums` and returns the result as an array.
