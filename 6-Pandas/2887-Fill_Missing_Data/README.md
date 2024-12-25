# 2887. Fill Missing Data

## Problem Statement

You are given a **0-indexed** array `data` containing integers and `null` values. Your task is to fill the missing values (`null`) in the array using the following rule:

- Replace each `null` with the **average** of its immediate neighbors (the previous and next elements in the array).  
- If a `null` is at the start or end of the array, replace it with the value of its only neighbor.  
- Round the resulting value to the nearest integer.

Return the modified array.

### Example 1:
Input: data = [1, null, 3, null, 5]  
Output: [1, 2, 3, 4, 5]  

Explanation:  
- The first `null` is replaced by the average of 1 and 3: `(1 + 3) / 2 = 2`.  
- The second `null` is replaced by the average of 3 and 5: `(3 + 5) / 2 = 4`.

### Example 2:
Input: data = [null, 4, null, 6]  
Output: [4, 4, 5, 6]  

Explanation:  
- The first `null` is replaced by its only neighbor, 4.  
- The second `null` is replaced by the average of 4 and 6: `(4 + 6) / 2 = 5`.

### Example 3:
Input: data = [null, null, 10]  
Output: [10, 10, 10]  

Explanation:  
- The first and second `null` are replaced by the only neighbor, 10.

### Constraints:
- `1 <= data.length <= 1000`
- The array contains integers and `null` values.
