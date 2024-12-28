# 1122. Relative Sort Array

## Problem

Given two arrays, `arr1` and `arr2`, the elements of `arr2` are distinct, and all elements in `arr2` are also in `arr1`. You need to sort the elements of `arr1` such that:

1. The elements of `arr1` appear in the same relative order as they do in `arr2`.
2. The elements that are not in `arr2` should be placed at the end of `arr1` in ascending order.

Write a function to implement the sorting logic as described above.

### Table: `arr1`

| Column Name  | Type    |
| ------------ | ------- |
| arr1         | int[]   |

- `arr1` is an array of integers.
  
### Table: `arr2`

| Column Name  | Type    |
| ------------ | ------- |
| arr2         | int[]   |

- `arr2` is an array of distinct integers, all elements of which are present in `arr1`.

### Constraints
- `1 <= arr1.length, arr2.length <= 1000`
- `0 <= arr1[i], arr2[i] <= 1000`
- All elements in `arr2` are distinct.
- Each element in `arr2` is guaranteed to be in `arr1`.

### Example

#### Input

```plaintext
arr1 = [28,6,22,8,44,17]
arr2 = [22,28,8,6]
Output
plaintext
Copy code
[22,28,8,6,17,44]
Explanation
Elements 22, 28, 8, 6 from arr1 are sorted based on their order in arr2.
Remaining elements 17, 44 are sorted in ascending order and placed at the end.
Example Usage
python
Copy code
arr1 = [28, 6, 22, 8, 44, 17]
arr2 = [22, 28, 8, 6]
print(relativeSortArray(arr1, arr2))  # Output: [22, 28, 8, 6, 17, 44]