# 2888. Reshape Data: Concatenate

## Problem Statement

You are given two **2D arrays** `matrix1` and `matrix2` with the same number of columns but different numbers of rows. Your task is to concatenate these two matrices vertically (i.e., add the rows of `matrix2` to the bottom of `matrix1`) and return the resulting matrix.

### Example 1:
Input:  
matrix1 = [[1, 2], [3, 4]]  
matrix2 = [[5, 6], [7, 8]]  

Output:  
[[1, 2], [3, 4], [5, 6], [7, 8]]  

Explanation:  
The rows of `matrix2` are added below the rows of `matrix1` to form the resulting matrix.

### Example 2:
Input:  
matrix1 = [[1, 2]]  
matrix2 = [[3, 4], [5, 6]]  

Output:  
[[1, 2], [3, 4], [5, 6]]  

Explanation:  
The rows of `matrix2` are added below the row of `matrix1`.

### Constraints:
- `1 <= matrix1.length, matrix2.length <= 1000`
- `1 <= matrix1[i].length, matrix2[i].length <= 1000`
- `matrix1[i].length == matrix2[i].length`
