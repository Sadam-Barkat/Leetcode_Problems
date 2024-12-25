# 2890. Reshape Data: Melt

## Problem Statement

You are given a **2D array** `data` where each row represents a record with multiple features (columns). Your task is to "melt" the data so that the columns become values in a new column, while keeping track of the associated row identifier and feature name.

### Example 1:
Input:
data = [[1, 2, 3], [4, 5, 6]]  
columns = ["A", "B", "C"]  

Output:
[  
  ["A", 1],  
  ["B", 2],  
  ["C", 3],  
  ["A", 4],  
  ["B", 5],  
  ["C", 6]  
]  

Explanation:  
- The first column (`A`, `B`, `C`) becomes the new feature column.  
- The second column (`1, 4`) becomes the value under "A".  
- The third column (`2, 5`) becomes the value under "B".  
- The fourth column (`3, 6`) becomes the value under "C".  

### Example 2:
Input:
data = [[1, 10], [2, 20], [3, 30]]  
columns = ["X", "Y"]  

Output:
[  
  ["X", 1],  
  ["Y", 10],  
  ["X", 2],  
  ["Y", 20],  
  ["X", 3],  
  ["Y", 30]  
]  

Explanation:  
- The first column (`X`) is paired with values 1, 2, and 3.  
- The second column (`Y`) is paired with values 10, 20, and 30.

### Constraints:
- `1 <= data.length <= 1000`
- `1 <= data[i].length <= 1000`
- `columns.length == data[i].length`
