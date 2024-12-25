# 2885. Rename Columns

## Problem Statement

You are given a **0-indexed** array `columns` containing strings, where each string represents the name of a column. Your task is to rename the columns such that:

- Each column name is unique.
- If there are duplicate column names, append a suffix `"(k)"` to the duplicates, where `k` is the smallest positive integer such that the resulting name is unique.

Return the renamed array of column names.

### Example 1:
Input: columns = ["a", "b", "a", "a", "b"]  
Output: ["a", "b", "a(1)", "a(2)", "b(1)"]  

Explanation:  
- The first occurrence of "a" remains as is.  
- The second occurrence of "a" is renamed to "a(1)".  
- The third occurrence of "a" is renamed to "a(2)".  
- The first occurrence of "b" remains as is.  
- The second occurrence of "b" is renamed to "b(1)".

### Example 2:
Input: columns = ["col", "col", "col", "col"]  
Output: ["col", "col(1)", "col(2)", "col(3)"]  

Explanation:  
Each duplicate occurrence of "col" is renamed with a suffix `(k)` to make it unique.

### Constraints:
- `1 <= columns.length <= 1000`
- `1 <= columns[i].length <= 10`
- `columns[i]` consists only of lowercase English letters.
