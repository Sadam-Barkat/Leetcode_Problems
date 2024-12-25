# 2889. Reshape Data: Pivot

## Problem Statement

You are given a **2D array** `data` containing rows of records, where each record has a category, value, and another feature. Your task is to pivot the data so that the unique values from the feature column become the new column headers, and the corresponding value in each row is placed under the appropriate column header.

### Example 1:
Input:
data = [["A", "X", 1], ["B", "X", 2], ["A", "Y", 3], ["B", "Y", 4]]  

Output:
[  
  ["A", 1, 3],  
  ["B", 2, 4]  
]  

Explanation:  
- The first column contains unique categories ("A" and "B").  
- The second and third columns are the values corresponding to features "X" and "Y".  

### Example 2:
Input:
data = [["A", "X", 5], ["A", "Y", 6], ["B", "X", 7], ["B", "Y", 8]]  

Output:
[  
  ["A", 5, 6],  
  ["B", 7, 8]  
]  

Explanation:  
- The first column contains categories "A" and "B".  
- The second column represents the values for feature "X", and the third column represents the values for feature "Y".  

### Constraints:
- `1 <= data.length <= 1000`
- `1 <= data[i].length <= 1000`
- `data[i][0]` is the category column (unique values), `data[i][1]` is the feature, and `data[i][2]` is the value to be pivoted.
