# Count Good Pairs

## Problem Statement
Given an array of integers `nums`, return the number of good pairs. A pair `(i, j)` is called good if:
- `nums[i] == nums[j]`
- `i < j`

## Examples

### Example 1
**Input**: 
- `nums = [1, 2, 3, 1, 1, 3]`

**Output**: 
- `4`

**Explanation**: The good pairs are:
- `(0, 3)`, `(0, 4)`, `(3, 4)`, `(2, 5)`

### Example 2
**Input**:
- `nums = [1, 1, 1, 1]`

**Output**:
- `6`

**Explanation**: All possible pairs are good:
- `(0, 1)`, `(0, 2)`, `(0, 3)`, `(1, 2)`, `(1, 3)`, `(2, 3)`

### Example 3
**Input**:
- `nums = [1, 2, 3]`

**Output**:
- `0`

**Explanation**: No pairs satisfy the condition.

## Constraints
- `1 <= nums.length <= 100`
- `1 <= nums[i] <= 100`

## Approach
- Iterate through the array using nested loops.
- Count pairs `(i, j)` where `nums[i] == nums[j]` and `i < j`.
- Return the total count of such pairs.

## Result
The solution provides an efficient way to find and count the number of good pairs in an array.
