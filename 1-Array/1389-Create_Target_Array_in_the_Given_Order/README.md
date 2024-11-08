# Insert Values into Target Array

## Problem Description

You are given two arrays of integers `nums` and `index`. Your task is to create a target array following these rules:

1. Initially, the target array is empty.
2. From left to right, read each element from `nums[i]` and `index[i]`. Insert the value `nums[i]` at position `index[i]` in the target array.
3. Repeat the previous step until all elements from `nums` and `index` have been processed.

The insertion operations are guaranteed to be valid, meaning `index[i]` will always be a valid position for insertion.

## Input

- `nums`: A list of integers where 1 <= `nums.length` <= 100, and 0 <= `nums[i]` <= 100.
- `index`: A list of integers where 1 <= `index.length` <= 100, and 0 <= `index[i]` <= i. The length of `index` is equal to the length of `nums`.

## Output

- Return the target array after performing all the insertions.

## Examples

### Example 1
**Input:**
nums = [0, 1, 2, 3, 4] index = [0, 1, 2, 2, 1]

makefile
Copy code

**Output:**
[0, 4, 1, 3, 2]

makefile
Copy code

### Example 2
**Input:**
nums = [1, 2, 3, 4, 0] index = [0, 1, 2, 3, 0]

makefile
Copy code

**Output:**
[0, 1, 2, 3, 4]

makefile
Copy code

### Example 3
**Input:**
nums = [1] index = [0]

makefile
Copy code

**Output:**
[1]

markdown
Copy code

## Constraints

- 1 <= nums.length, index.length <= 100
- nums.length == index.length
- 0 <= nums[i] <= 100
- 0 <= index[i] <= i

## Approach

1. Start with an empty `target` array.
2. For each element in `nums` and the corresponding `index`, insert the value at the specified index in the `target` array.
3. Return the `target` array after all operations are complete.

## Time Complexity

- The time complexity for each insertion is O(n), where n is the length of the `target` array at that point. So the overall complexity is O(n^2).

## Space Complexity

- The space complexity is O(n), as we need to store the `target` array of size `n`.