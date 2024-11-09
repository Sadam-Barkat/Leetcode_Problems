# Matrix Transpose

## Problem Overview

Given a 2D integer array `matrix`, the task is to return the **transpose** of the matrix. The transpose of a matrix is obtained by flipping the matrix over its **main diagonal**, switching its row and column indices.

### Definition of Transpose:
- The element at position `(i, j)` in the original matrix becomes the element at position `(j, i)` in the transposed matrix.

### Example 1:

**Input:**
```python
matrix = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]
Output:

python
Copy code
[
  [1, 4, 7],
  [2, 5, 8],
  [3, 6, 9]
]
Example 2:
Input:

python
Copy code
matrix = [
  [1, 2, 3],
  [4, 5, 6]
]
Output:

python
Copy code
[
  [1, 4],
  [2, 5],
  [3, 6]
]
Problem Constraints
m == matrix.length
n == matrix[i].length
1 <= m, n <= 1000
1 <= m * n <= 105
-109 <= matrix[i][j] <= 109